from app.services.sleeper_api_client import sleeper_client
from fastapi import APIRouter, Query, HTTPException, Depends, Cookie
from app.services.supabase_client import get_supabase
import app.services.espn as ESPNService
from supabase._async.client import AsyncClient
from typing import Optional
import app.services.auth as AuthService
import asyncio

router = APIRouter()

@router.get('/leagues/{user_id}')
async def get_league_info(user_id: str, current_user = Depends(AuthService.get_current_user), supabase: AsyncClient = Depends(get_supabase)):
    try:
        sleeper_info, espn_info = await asyncio.gather(
            sleeper_client.get_sleeper_user_info(user_id, supabase),
            ESPNService.get_espn_user_info(user_id, supabase)
        )

        sleeper_leagues = []
        espn_leagues = []

        for entry in sleeper_info:
            league = await sleeper_client.get_sleeper_roster_by_id(entry['sleeper_user_id'], entry['year'])
            sleeper_leagues.append(league)

        for entry in espn_info:
            league = await ESPNService.get_espn_league_data(
                entry['league_id'],
                entry['year'],
                entry['espn_s2'],
                entry['swid'],
                entry['team_id']
            )
            espn_leagues.append(league)

        return {"sleeper": sleeper_leagues[0], "espn": espn_leagues}
    
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

