from fastapi import APIRouter, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
from espn_api.football import League

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
    
@router.get('/espn/leagues/scores/{week}')
async def get_league_scores_by_week(week: int, manager: LeagueManager = Depends(get_league_manager)):
    if not manager.league:
        raise HTTPException(status_code=404, detail="Your league must be connected first!")
    
    if week < 1 or not week:
        raise HTTPException(status_code=400, detail="Please provide the week!")

    # create Pydantic models for the objects that will be returned for cleaner handling
    box_scores = manager.league.box_scores(week)
    formatted_box_scores = []
    for matchup in box_scores:
        formatted_box_scores.append({
            "home_team": {
                "name": matchup.home_team.team_name,
                "score": matchup.home_score
            },
            "away_team": {
                "name": matchup.away_team.team_name,
                "score": matchup.away_score
            }
        })
    
    return JSONResponse({"week": week, "scores": formatted_box_scores}, status_code=200)