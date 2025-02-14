from fastapi import Depends, HTTPException
import httpx
from app.services.supabase_client import get_supabase
from supabase._async.client import AsyncClient
from app.models.sleeper import SleeperLeague
import asyncio

class SleeperAPIClient:
    BASE_URL = 'https://api.sleeper.app/v1'

    def __init__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL)    
    
    async def get_sleeper_user_by_username(self, username: str):
        response = await self.client.get(f'/user/{username}')
        return response.json()

    async def get_sleeper_user_by_id(self, user_id: str):
        response = await self.client.get(f'/user/{user_id}')
        return response.json()
    
    async def get_sleeper_user_info(self, user_id: str, supabase: AsyncClient = Depends(get_supabase)):
        try:
            sleeper_leagues = await supabase.table('sleeper_leagues').select('sleeper_user_id', 'year').eq('id', user_id).execute()
            return sleeper_leagues.data
        except Exception as e:
            return HTTPException(status_code=500, detail=str(e))
    
    async def get_sleeper_user_id(self, username: str):
        response = await self.get_sleeper_user_by_username(username)
        return response.json().get('user_id')
    
    async def get_sleeper_leagues(self, user_id: str, season: str):
        print('get_sleeper_leagues')
        response = await self.client.get(f'/user/{user_id}/leagues/nfl/{season}')
        return response.json()
    
    async def get_sleeper_league_by_id(self, league_id: str):
        print('get_sleeper_league_by_id')
        response = await self.client.get(f'/league/{league_id}')
        return response.json()
    
    async def get_sleeper_league_rosters(self, league_id: str):
        print('get_sleeper_league_rosters')
        response = await self.client.get(f'/league/{league_id}/rosters')
        return response.json()
    
    async def get_sleeper_roster_by_id(self, user_id: str, year: str):
        # get the user's leagues for a year
        leagues = await self.get_sleeper_leagues(user_id, year)

        data = []

        for league in leagues:
            # return all rosters and users in the league
            rosters, users = await asyncio.gather(
                self.get_sleeper_league_rosters(league.get('league_id')),
                self.get_sleeper_league_teams(league.get('league_id'))
            )
            # get the roster associated to the user_id
            roster = next(
                (roster for roster in rosters if roster['owner_id'] == user_id),
                None
            )
            # get the user's team associated to the user_id
            user = next(
                (user for user in users if user['user_id'] == user_id)
            )
            
            data.append(SleeperLeague(
                name=league.get('name'),
                num_teams=int(league['settings']['num_teams']),
                wins=int(roster['settings']['wins']),
                losses=int(roster['settings']['losses']),
                team_name=user.get('display_name')
            ))

        return data
    
    async def get_sleeper_league_teams(self, league_id: str):
        print('get_sleeper_league_users')
        response = await self.client.get(f'/league/{league_id}/users')
        return response.json()
    
    async def get_sleeper_league_matchups(self, league_id: str, week: str):
        print('get_sleeper_league_matchups')
        response = await self.client.get(f'/league/{league_id}/matchups/{week}')
        return response.json()
    
    async def get_sleeper_winners_bracket(self, league_id: str):
        print('get_sleeper_winners_bracket')
        response = await self.client.get(f'/league/{league_id}/winners_bracket')
        return response.json()
    
    async def get_sleeper_losers_bracket(self, league_id: str):
        print('get_sleeper_losers_bracket')
        response = await self.client.get(f'/league/{league_id}/losers_bracket')
        return response.json()
    
    async def get_sleeper_transactions_by_week(self, league_id: str, week: str):
        print('get_sleeper_transactions_by_week')
        response = await self.client.get(f'/league/{league_id}/transactions/{week}')
        return response.json()
    
    async def get_sleeper_traded_picks(self, league_id: str):
        print('get_sleeper_traded_picks')
        response = await self.client.get(f'/league/{league_id}/traded_picks')
        return response.json()
    
    async def get_league_state(self, league_name: str):
        print('get_league_state')
        response = await self.client.get(f'/state/{league_name}')
        return response.json()
    
    async def get_sleeper_user_drafts(self, user_id: str, season: str):
        print('get_user_drafts')
        response = await self.client.get(f'/user/{user_id}/drafts/nfl/{season}')
        return response.json()
    
    async def get_sleeper_league_drafts(self, league_id: str):
        print('get_league_drafts')
        response = await self.client.get(f'/league/{league_id}/drafts')
        return response.json()
    
    async def get_sleeper_draft(self, draft_id: str):
        print('get_sleeper_draft')
        response = await self.client.get(f'/draft/{draft_id}')
        return response.json()
    
    async def get_sleeper_draft_picks(self, draft_id: str):
        print('get_sleeper_draft_picks')
        response = await self.client.get(f'/draft/{draft_id}/picks')
        return response.json()

    async def get_sleeper_draft_traded_picks(self, draft_id: str):
        print('get_sleeper_draft_traded_picks')
        response = await self.client.get(f'/draft/{draft_id}/traded_picks')
        return response.json()
    
    async def get_all_sleeper_players(self, supabase: AsyncClient = Depends(get_supabase)):
        print('get_all_sleeper_players')
        print(supabase)
        response = await supabase.table('players').select("*").execute()
        return response.data
    
    async def get_sleeper_player_by_name(self, first_name: str, last_name: str, supabase: AsyncClient = Depends(get_supabase)):
        print('get_sleeper_player_by_name')
        response = await supabase.table('players').select('*').ilike('first_name', first_name).ilike('last_name', last_name).execute()
        return response.data
    
    async def get_sleeper_player_by_id(self, player_id: str, supabase: AsyncClient = Depends(get_supabase)):
        print('get_sleeper_player_by_id')
        response = await supabase.table('players').select('*').ilike('player_id', player_id).execute()
        return response.data
    
    async def get_sleeper_trending_players(self, type: str, lookback_hours: int, limit: int):
        print('get_sleeper_trending_players')
        response = await self.client.get(f'/players/nfl/trending/{type}?lookback_hours={lookback_hours}&limit={limit}')
        return response.json()

sleeper_client = SleeperAPIClient()