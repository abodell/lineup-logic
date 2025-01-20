import httpx
import os
from supabase import create_client, Client

def get_nfl_scoreboard() -> dict:
    nfl_scoreboard = client.get('/s/scoreboard?lang=en-US&region=US&tz=America%2FNew_York&ysp_redesign=1&ysp_platform=desktop&leagues=nfl&week=current&season=current')
    return nfl_scoreboard.json()

if __name__ == '__main__':
    client = httpx.Client(base_url = 'https://api-secure.sports.yahoo.com/v1/editorial')
    print(get_nfl_scoreboard())