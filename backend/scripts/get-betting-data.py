import httpx
import os
from supabase import create_client, Client

def get_nfl_betting_lines() -> dict:
    nfl_betting_lines = client.get('/s/scoreboard?lang=en-US&region=US&tz=America%2FNew_York&ysp_redesign=1&ysp_platform=desktop&leagues=nfl&week=current&season=current')
    return nfl_betting_lines.json().get('service').get('scoreboard').get('gameodds')

def parse_nfl_betting_data(betting_lines: dict) -> dict:
    lines = {}

    fields_to_extract = ["away_ml", "home_ml", "away_spread", "away_line", "home_spread", 
                         "home_line", "total", "over_line", "under_line"]
    
    for game_id, game_data in betting_lines.items():
        lines[game_id] = {key: game_data.get('101').get(key) for key in fields_to_extract}
        lines[game_id]['game_id'] = game_id
    
    return lines

def insert_to_supabase(betting_lines: dict):
    try:
        records = []
        for game in betting_lines.values():
            records.append(game)
        
        response = supabase.table('betting_lines').upsert(records).execute()
        print('Data inserted to supabase successfully!')

    except Exception as e:
        print(f'Error inserting to supabase: {e}')

if __name__ == '__main__':
    client = httpx.Client(base_url = 'https://api-secure.sports.yahoo.com/v1/editorial')
    if not os.getenv('DATABASE_URL') or not os.getenv('DATABASE_KEY'):
        print('Environment Secrets not fetched!')
    supabase: Client = create_client(os.getenv('DATABASE_URL'), os.getenv('DATABASE_KEY'))
    betting_lines = get_nfl_betting_lines()
    parsed_lines = parse_nfl_betting_data(betting_lines)
    try:
        insert_to_supabase(parsed_lines)
    except Exception as e:
        print(f"Error: {e}")