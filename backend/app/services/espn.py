from fastapi import Depends, HTTPException
from app.services.supabase_client import get_supabase
from supabase._async.client import AsyncClient
from espn_api.football import League
import app.services.auth as AuthService

async def get_espn_league(supabase: AsyncClient = Depends(get_supabase), current_user = Depends(AuthService.get_current_user)) -> League:
    try:
        result = await supabase.table('espn_leagues').select('*').eq('id', current_user.id).execute()

        if not result.data:
            raise HTTPException(status_code=404, detail="ESPN League Credentials Not Found.  Please connect your league first!")
        
        credentials = result.data[0]

        return League(
            league_id=credentials['league_id'],
            year=credentials['year'],
            espn_s2=credentials['espn_s2'],
            swid=credentials['swid']
        )
    
    except Exception as e:
        return HTTPException(status_code=500, detail = str(e))

async def get_espn_user_info(user_id: str, supabase: AsyncClient = Depends(get_supabase)):
    try:
        espn_leagues = await supabase.table('espn_leagues').select('league_id', 'year', 'espn_s2', 'swid').eq('id', user_id).execute()
        return espn_leagues.data
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
async def find_team_by_name(team_list: list, team_name: str):
    for team in team_list:
        if team.__dict__.get('team_name') == team_name:
            return team.__dict__.get('team_id')
    return None

async def get_owner_id(team_list, team_name):
    for team in team_list:
        if team.__dict__.get('team_name') == team_name:
            return team.__dict__.get('owners')[0].get('id')
    return None