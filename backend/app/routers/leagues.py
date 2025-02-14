from app.services.sleeper_api_client import sleeper_client
from fastapi import APIRouter, Query, HTTPException, Depends, Cookie
from app.services.supabase_client import get_supabase
import app.services.espn as ESPNService
from supabase._async.client import AsyncClient
from typing import Optional
import app.services.auth as AuthService

router = APIRouter()

@router.get('/leagues/{user_id}')
async def get_league_info(user_id: str, current_user = Depends(AuthService.get_current_user), supabase: AsyncClient = Depends(get_supabase)):
    try:
        sleeper_leagues = await sleeper_client.get_sleeper_user_info(user_id, supabase)
        espn_leagues = await ESPNService.get_espn_user_info(user_id, supabase)


        return {"sleeper": sleeper_leagues, "espn": espn_leagues}
    
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

