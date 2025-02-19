from fastapi import Depends, HTTPException, APIRouter
from supabase._async.client import AsyncClient
from app.services.supabase_client import get_supabase

router = APIRouter()

@router.get('/betting/recent')
async def get_recent_betting_data(supabase: AsyncClient = Depends(get_supabase)):
    try:
        response = await supabase.table('latest_betting_lines').select('away_ml, home_ml, away_spread, home_spread, away_line, home_line, total, over_line, under_line, ' 
                    'game:games!game_id(home_team_id, away_team_id, start_time, home_team:teams!Games_home_team_id_season_fkey(team_abbr), away_team:teams!Games_away_team_id_season_fkey(team_abbr)), '
                    'winning_ml_bet, winning_spread_bet, winning_total_bet') \
                    .limit(10) \
                    .execute()

        return response.data

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))