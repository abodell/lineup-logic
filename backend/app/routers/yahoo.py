from fastapi import APIRouter, Query, HTTPException, Depends
from supabase._async.client import AsyncClient
from app.services.supabase_client import create_supabase
from typing import Optional

router = APIRouter()

@router.get('/yahoo/teams')
async def get_teams(team_id: Optional[str] = Query(None),
                    conference_id: Optional[int] = Query(None),
                    division_id: Optional[int] = Query(None),
                    season: Optional[int] = Query(None),
                    supabase: AsyncClient = Depends(create_supabase)
    ):
        res = await supabase.table('teams').select('*').execute()
        return res