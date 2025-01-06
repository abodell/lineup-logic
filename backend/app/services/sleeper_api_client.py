import httpx
from app.services.supabase_client import create_supabase

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
    
    async def get_sleeper_league_users(self, league_id: str):
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
    
    async def get_all_sleeper_players(self):
        print('get_all_sleeper_players')
        supabase_async = await create_supabase()
        response = await supabase_async.table('players').select("*").execute()
        return response.data
    
    async def get_sleeper_player_by_name(self, first_name: str, last_name: str):
        print('get_sleeper_player_by_name')
        supabase_async = await create_supabase()
        response = await supabase_async.table('players').select('*').ilike('first_name', first_name).ilike('last_name', last_name).execute()
        return response.data
    
    async def get_sleeper_player_by_id(self, player_id: str):
        print('get_sleeper_player_by_id')
        supabase_async = await create_supabase()
        response = await supabase_async.table('players').select('*').ilike('player_id', player_id).execute()
        return response.data


sleeper_client = SleeperAPIClient()