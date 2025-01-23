from fastapi import APIRouter, Query, HTTPException, Depends
from supabase._async.client import AsyncClient
from app.services.supabase_client import create_supabase
from typing import Optional

router = APIRouter()

@router.get('/yahoo/nfl/teams')
async def get_teams(team_id: Optional[str] = Query(None),
                    conference_id: Optional[int] = Query(None),
                    division_id: Optional[int] = Query(None),
                    season: Optional[int] = Query(None),
                    supabase: AsyncClient = Depends(create_supabase)
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

@router.get('/yahoo/nfl/teams/{team_id}')
async def get_team_by_id(team_id: str, supabase: AsyncClient = Depends(create_supabase)):
        query = supabase.table('teams').select('*').filter('team_id', 'eq', team_id)
        res = await query.execute()
        return res

@router.get('/yahoo/nfl/betting/lines')
async def get_betting_lines(game_id: Optional[str] = Query(None), supabase: AsyncClient = Depends(create_supabase)):
        query = supabase.table('betting_lines').select('*')
        if game_id:
            query.filter('game_id', 'eq', game_id)
        res = await query.execute()
        return res

@router.get('yahoo/nfl/betting/lines/{game_id}')
async def get_betting_lines_by_game_id(game_id: str, supabase: AsyncClient = Depends(create_supabase)):
        query = supabase.table('betting_lines').select('*').filter('game_id', 'eq', game_id)
        res = await query.execute()
        return res

@router.get('/yahoo/nfl/current-week')
async def get_current_week(supabase: AsyncClient = Depends(create_supabase)):
        query = supabase.table('games').select('week_number').order('week_number').limit(1)
        res = await query.execute()
        return res

@router.get('/yahoo/nfl/biggest-favorites')
async def get_biggest_favorites(count: Optional[int] = Query(None), week: Optional[int] = Query(None), supabase: AsyncClient = Depends(create_supabase)):
    if not week:
        current_week = await get_current_week(supabase)
    
    return current_week