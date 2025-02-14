from fastapi import APIRouter, Query, HTTPException, Depends, Cookie
from app.models.espn import (
    MatchupScoreboard, TeamScoreboard, 
    BoxPlayer, WeekScoreboard, LeagueTeams, 
    ESPNTeam, PlayerInfo, TeamInfo, TeamInfoList, 
    DraftPick, Draft, PlayerList, Transaction, 
    RecentActivity, RecentActivityList)
from fastapi.responses import JSONResponse
from espn_api.football import League
from espn_api.football.box_score import BoxScore
from typing import List, Literal, Optional
from app.services.supabase_client import get_supabase
import app.services.espn as ESPNService
from supabase._async.client import AsyncClient
import app.services.auth as AuthService


router = APIRouter()

class LeagueManager:
    league: League = None

league_manager = LeagueManager()

def get_league_manager():
    return league_manager
# I think I need to refactor how this works
@router.get('/espn/leagues/connect')
async def connect_league(league_id: str = Query(None), year: int = Query(None), espn_s2: str = Query(None), swid: str = Query(None), manager: LeagueManager = Depends(get_league_manager)):
    if not league_id or not year or not espn_s2 or not swid:
        raise HTTPException(status_code=400, detail="Must provide league_id, year, espn_s2, and swid")
    
    try:
        manager.league = League(league_id = league_id, year = year, espn_s2 = espn_s2, swid = f'{{{swid}}}')
        res_content = {"message": "Successfully connected to your league!"}
        return JSONResponse(content = res_content, status_code=200)
    except Exception as e:
        raise Exception(e)

@router.post('/espn/leagues/connect')
async def save_espn_league_info(
    league_id: str = Query(None),
    year: int = Query(None),
    espn_s2: str = Query(None),
    swid: str = Query(None),
    team_name: str = Query(None),
    supabase: AsyncClient = Depends(get_supabase),
    current_user = Depends(AuthService.get_current_user)
):
    if not league_id or not year or not espn_s2 or not swid or not team_name:
        raise HTTPException(status_code=400, detail="Must provide league_id, year, espn_s2, swid, and team_name")
    
    try:
        league = League(league_id = league_id, year = year, espn_s2 = espn_s2, swid = f'{{{swid}}}')

        if league:
            team_id = await ESPNService.find_team_by_name(league.teams, team_name)

            espn_data = {
                "id": current_user.id,
                "league_id": league_id,
                "year": year,
                "espn_s2": espn_s2,
                "swid": swid,
                "team_id": team_id
            }

            result = await supabase.table('espn_leagues').upsert(espn_data).execute()
            return result.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/espn/userinfo/{user_id}')
async def get_espn_user_info(user_id: str, supabase: AsyncClient = Depends(get_supabase)):
    try:
        result = await supabase.table('espn_leagues').select('league_id', 'espn_s2', 'swid', 'year').eq('id', user_id).execute()
        return result.data
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@router.get('/espn/current-week')
async def get_current_week(league: League = Depends(ESPNService.get_espn_league)):
    if not league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    return JSONResponse(content = {"current_week": league.current_week})

@router.get('/espn/leagues/recent-activity')
async def get_recent_activity(size: int = Query(25), msg_type: str = Query(None), offset: int = Query(0), manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    params = {
        "size": size,
        "msg_type": msg_type,
        "offset": offset
    }

    params = {key: value for key, value in params.items() if value is not None}
    
    transactions = []

    for activity in manager.league.recent_activity(**params):
        transactions.append(RecentActivity(
            actions = [Transaction(
                team = TeamInfo.model_validate(sub_activity[0], from_attributes = True),
                transaction_type = sub_activity[1],
                player = PlayerInfo.model_validate(sub_activity[2], from_attributes = True),
                additional_data = sub_activity[3]
            ) for sub_activity in activity.__dict__['actions']],
            date = activity.__dict__['date']
        ))

    return RecentActivityList(transactions = transactions)

@router.get('/espn/leagues/draft')
async def get_draft(manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    picks = [DraftPick(
        **pick.__dict__,
        team_name = pick.team.team_name
    ) for pick in manager.league.draft]

    return Draft(draft = picks)

@router.get('/espn/leagues/teams/rankings/{week}')
async def get_team_rankings(week: int, manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    rankings = [TeamInfo.model_validate(team[1], from_attributes=True) for team in manager.league.power_rankings(week)]

    return TeamInfoList(teams = rankings)

@router.get('/espn/leagues/teams/standings')
async def get_league_standings(week: int = Query(None), manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    standings = []
    
    if week:
        for team in manager.league.standings_weekly(week):
            standings.append(TeamInfo.model_validate(team, from_attributes = True))
    else:
        for team in manager.league.standings():
            standings.append(TeamInfo.model_validate(team, from_attributes = True))
    
    return TeamInfoList(teams = standings)
    
@router.get('/espn/leagues/teams/{id}')
async def get_team_by_id(id: int, manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    team = manager.league.get_team_data(id)

    return ESPNTeam(
        **{key: value for key, value in team.__dict__.items() if key != 'schedule' and key != 'roster'},  # Unpack all except schedule and roster
        schedule=[TeamInfo.model_validate(opponent, from_attributes=True) for opponent in team.schedule], # Override schedule
        roster = [PlayerInfo.model_validate(player, from_attributes=True) for player in team.roster]
    )

@router.get('/espn/leagues/teams/scoring/{type}')
async def get_scoring_data(type: Literal["most", "least", "against"], manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    team: TeamInfo

    if type == "least":
        team = manager.league.least_scorer()
    elif type == "most":
        team = manager.league.top_scorer()
    elif type == "against":
        team = manager.league.most_points_against()
    
    return TeamInfo.model_validate(team, from_attributes = True)
    
@router.get('/espn/leagues/teams')
async def get_teams(manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    team_list = [ESPNTeam(
        **{key: value for key, value in team.__dict__.items() if key != 'schedule' and key != 'roster'},  # Unpack all except schedule and roster
        schedule=[TeamInfo.model_validate(opponent, from_attributes=True) for opponent in team.schedule], # Override schedule
        roster = [PlayerInfo.model_validate(player, from_attributes=True) for player in team.roster] # override roster
    ) for team in manager.league.teams]

    return LeagueTeams(teams = team_list)

@router.get('/espn/leagues/waivers')
async def get_waiver_wire(week: int = Query(None), size: int = Query(None), position: str = Query(None), position_id: int = Query(None), manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    params = {
        "week": week,
        "size": size,
        "position": position,
        "position_id": position_id
    }

    params = {key: value for key, value in params.items() if value is not None}

    waiver_wire = [PlayerInfo.model_validate(player, from_attributes = True) for player in manager.league.free_agents(**params)]

    return PlayerList(waiver_wire = waiver_wire)

@router.get('/espn/leagues/players')
async def get_player_info(name: str = Query(None), player_id: int = Query(None), manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    params = {
        "name": name,
        "playerId": player_id
    }

    params = {key: value for key, value in params.items() if value is not None}

    player = manager.league.player_info(**params)

    return PlayerInfo.model_validate(player, from_attributes = True)

@router.get('/espn/leagues/scoreboard/{week}')
async def get_league_scores_by_week(week: int, manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    if week < 1 or not week:
        raise HTTPException(status_code=400, detail="Please provide the week!")

    # create Pydantic models for the objects that will be returned for cleaner handling
    matchups: List[BoxScore] = manager.league.box_scores(week)
    scoreboard = []
    for matchup in matchups:
        scoreboard.append(MatchupScoreboard(
            home_team = TeamScoreboard(
                team_name = matchup.home_team.team_name,
                team_score = matchup.home_score,
                projected = matchup.home_projected,
                lineup = [BoxPlayer(
                    name = player.name,
                    slot_position = player.slot_position,
                    points = player.points,
                    projected_points = player.projected_points,
                    pro_opponent = player.pro_opponent,
                    pro_pos_rank = player.pro_pos_rank,
                    game_played = player.game_played,
                    game_date = getattr(player, 'game_date', None),
                    on_bye_week = player.on_bye_week,
                    active_status = player.active_status
                ) for player in matchup.home_lineup]
            ),
            away_team = TeamScoreboard(
                team_name = matchup.away_team.team_name,
                team_score = matchup.away_score,
                projected = matchup.away_projected,
                lineup = [BoxPlayer(
                    name = player.name,
                    slot_position = player.slot_position,
                    points = player.points,
                    projected_points = player.projected_points,
                    pro_opponent = player.pro_opponent,
                    pro_pos_rank = player.pro_pos_rank,
                    game_played = player.game_played,
                    game_date = getattr(player, 'game_date', None),
                    on_bye_week = player.on_bye_week,
                    active_status = player.active_status
                ) for player in matchup.away_lineup]
            )
        ))

    return WeekScoreboard(scores=scoreboard)