from fastapi import APIRouter, Query, HTTPException, Depends
from app.models.espn import MatchupScoreboard, TeamScoreboard, BoxPlayer, WeekScoreboard, LeagueTeams, ESPNTeam, PlayerInfo, TeamInfo, LeagueRankings, DraftPick, Draft
from fastapi.responses import JSONResponse
from espn_api.football import League
from espn_api.football.box_score import BoxScore
from typing import List


router = APIRouter()

class LeagueManager:
    league: League = None

league_manager = LeagueManager()

def get_league_manager():
    return league_manager

@router.get('/espn/leagues/connect')
async def get_league(league_id: str = Query(None), year: int = Query(None), espn_s2: str = Query(None), swid: str = Query(None), manager: LeagueManager = Depends(get_league_manager)):
    if not league_id or not year or not espn_s2 or not swid:
        raise HTTPException(status_code=400, detail="Must provide league_id, year, espn_s2, and swid")
    
    try:
        manager.league = League(league_id = league_id, year = year, espn_s2 = espn_s2, swid = f'{{{swid}}}')
        res_content = {"message": "Successfully connected to your league!"}
        return JSONResponse(content = res_content, status_code=200)
    except Exception as e:
        raise Exception(e)

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

    return LeagueRankings(teams = rankings)

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
    
    return LeagueRankings(teams = standings)
    
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