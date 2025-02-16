from fastapi import APIRouter, Query, HTTPException, Depends
from supabase._async.client import AsyncClient
from app.services.supabase_client import get_supabase
from typing import Optional

router = APIRouter()

@router.get('/nfl/teams')
async def get_teams(team_id: Optional[str] = Query(None),
                    conference_id: Optional[int] = Query(None),
                    division_id: Optional[int] = Query(None),
                    season: Optional[int] = Query(None),
                    supabase: AsyncClient = Depends(get_supabase)
    ):
        query = supabase.table('teams').select('*')
        if team_id:
                query.filter('team_id', 'eq', team_id)
        if conference_id:
                query.filter('conference_id', 'eq', conference_id)
        if division_id:
                query.filter('division_id', 'eq', division_id)
        if season:
                query.filter('season', 'eq', season)
        
        res = await query.execute()
        return res

@router.get('/nfl/teams/{team_id}')
async def get_team_by_id(team_id: str, supabase: AsyncClient = Depends(get_supabase)):
        query = supabase.table('teams').select('*').filter('team_id', 'eq', team_id)
        res = await query.execute()
        return res

@router.get('/nfl/betting/lines')
async def get_betting_lines(game_id: Optional[str] = Query(None), supabase: AsyncClient = Depends(get_supabase)):
        query = supabase.table('betting_lines').select('*')
        if game_id:
            query.filter('game_id', 'eq', game_id)
        res = await query.execute()
        return res

@router.get('/nfl/betting/lines/{game_id}')
async def get_betting_lines_by_game_id(game_id: str, supabase: AsyncClient = Depends(get_supabase)):
        query = supabase.table('betting_lines').select('*').filter('game_id', 'eq', game_id)
        res = await query.execute()
        return res

@router.get('/nfl/current-week')
async def get_current_week(supabase: AsyncClient = Depends(get_supabase)):
        query = supabase.table('games').select('week_number').order('week_number').limit(1)
        res = await query.execute()
        return res

@router.get('/nfl/recent-games')
async def get_recent_games(supabase: AsyncClient = Depends(get_supabase)):
        try:
                response = await supabase.table('games').select("*, home_team:teams!Games_home_team_id_season_fkey(team_abbr), away_team:teams!Games_away_team_id_season_fkey(team_abbr)").limit(10).execute()

                return response.data
        except Exception as e:
                return HTTPException(status_code=500, detail=str(e))