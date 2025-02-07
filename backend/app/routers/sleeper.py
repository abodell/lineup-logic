from app.services.sleeper_api_client import sleeper_client
from fastapi import APIRouter, Query, HTTPException, Depends, Cookie
from app.services.supabase_client import get_supabase
from supabase._async.client import AsyncClient
from typing import Optional

router = APIRouter()

@router.get('/sleeper/user', tags=['sleeper'])
async def get_user(username: str = Query(None), user_id: str = Query(None)):
    if not username and not user_id:
        raise HTTPException(status_code=400, detail="Must provide username or user_id!")

    try:
        if username:
            user = await sleeper_client.get_sleeper_user_by_username(username)
            return user
        
        if user_id:
            user = await sleeper_client.get_sleeper_user_by_id(user_id)
            return user
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.post('/sleeper/user', tags=['sleeper'])
async def save_sleeper_user(username: str = Query(None), supabase: AsyncClient = Depends(get_supabase), access_token: Optional[str] = Cookie(None, alias="access_token")):
    if not username:
        raise HTTPException(status_code=400, detail="Must provide username or user_id!")

    if not access_token:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    
    try:
        user = await supabase.auth.get_user(access_token)
        user_id = user.user.id

        sleeper_user = await sleeper_client.get_sleeper_user_by_username(username)
        
        sleeper_data = {
            'id': user_id,
            'sleeper_username': sleeper_user.get('username'),
            'sleeper_user_id': sleeper_user.get('user_id')
        }

        result = await supabase.table("sleeper_users").upsert(sleeper_data).execute()
        return result.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/sleeper/users/{user_id}/drafts/{season}')
async def get_user_drafts(user_id: str, season: str):
    if not user_id:
        raise HTTPException(status_code=400, detail="Must provide user_id")
    elif not season:
        raise HTTPException(status_code=400, detail="Must provide the season year (e.g. 2023)")
    
    try:
        drafts = await sleeper_client.get_sleeper_user_drafts(user_id, season)
        return drafts
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/users/{user_id}/leagues/{season}')
async def get_user_leagues(user_id: str, season: str):
    if not user_id:
        raise HTTPException(status_code=400, detail="Must provide user_id")
    elif not season:
        raise HTTPException(status_code=400, detail="Must provide the season year (e.g. 2023)")
    
    try:
        leagues = await sleeper_client.get_sleeper_leagues(user_id, season)
        return leagues
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/rosters/{league_id}')
async def get_league_rosters(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        rosters = await sleeper_client.get_sleeper_league_rosters(league_id)
        return rosters
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/leagues/{league_id}/matchups/{week}')
async def get_league_matchups(league_id: str, week: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    elif not week:
        raise HTTPException(status_code=400, detail="Must provide week")
    
    try:
        matchups = await sleeper_client.get_sleeper_league_matchups(league_id, week)
        return matchups
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/leagues/{league_id}/transactions/{week}')
async def get_league_transactions(league_id: str, week: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide a league_id")
    elif not week:
        raise HTTPException(status_code=400, detail="Must provide week")
    
    try:
        transactions = await sleeper_client.get_sleeper_transactions_by_week(league_id, week)
        return transactions
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/leagues/{league_id}/users')
async def get_league_users(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        users = await sleeper_client.get_sleeper_league_users(league_id)
        return users
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/leagues/{league_id}/traded_picks')
async def get_traded_picks(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        traded_picks = await sleeper_client.get_sleeper_traded_picks(league_id)
        return traded_picks
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/leagues/{league_id}/drafts')
async def get_league_drafts(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        drafts = await sleeper_client.get_sleeper_league_drafts(league_id)
        return drafts
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/leagues/{league_id}')
async def get_league_by_id(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        league = await sleeper_client.get_sleeper_league_by_id(league_id)
        return league
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/playoffs/{league_id}/winners')
async def get_winners_bracket(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        winners = await sleeper_client.get_sleeper_winners_bracket(league_id)
        return winners
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/playoffs/{league_id}/losers')
async def get_losers_bracket(league_id: str):
    if not league_id:
        raise HTTPException(status_code=400, detail="Must provide league_id")
    
    try:
        losers = await sleeper_client.get_sleeper_losers_bracket(league_id)
        return losers
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/state/{league_name}')
async def get_league_state(league_name: str):
    if not league_name:
        raise HTTPException(status_code=400, detail="Must provide league_name")
    
    try:
        state = await sleeper_client.get_league_state(league_name)
        return state
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/drafts/{draft_id}/picks')
async def get_draft_picks(draft_id: str):
    if not draft_id:
        raise HTTPException(status_code=400, detail="Must provide draft_id")
    
    try:
        picks = await sleeper_client.get_sleeper_draft_picks(draft_id)
        return picks
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/drafts/{draft_id}/traded_picks')
async def get_traded_draft_picks(draft_id: str):
    if not draft_id:
        raise HTTPException(status_code=400, detail="Must provide draft_id")
    
    try:
        picks = await sleeper_client.get_sleeper_draft_traded_picks(draft_id)
        return picks
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/drafts/{draft_id}')
async def get_draft(draft_id: str):
    if not draft_id:
        raise HTTPException(status_code=400, detail="Must provide draft_id")
    
    try:
        draft = await sleeper_client.get_sleeper_draft(draft_id)
        return draft
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/sleeper/players/trending/{type}')
async def get_trending_players(type: str, lookback_hours: int = Query(None), limit: int = Query(None)):
    if not type:
        raise HTTPException(status_code=400, detail="Must provide a type (add/drop)!")
    
    if not lookback_hours:
        lookback_hours = 24
    
    if not limit:
        limit = 25
    
    try:
        trending_players = await sleeper_client.get_sleeper_trending_players(type, lookback_hours, limit)
        return trending_players
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.get('/sleeper/players')
async def get_players(first_name: str = Query(None), last_name: str = Query(None), player_id: str = Query(None), supabase: AsyncClient = Depends(get_supabase)):
    try:
        if (first_name and last_name):
            players = await sleeper_client.get_sleeper_player_by_name(first_name, last_name, supabase)
        elif (player_id):
            players = await sleeper_client.get_sleeper_player_by_id(player_id, supabase)
        else:
            players = await sleeper_client.get_all_sleeper_players(supabase)
        
        if not players:
            raise HTTPException(status_code=404, detail="No players found!")
        return players
    except HTTPException as e:
        print("Error occured:", e)
        raise HTTPException(status_code=e, detail=e.detail)