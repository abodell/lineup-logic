import httpx
import os
from supabase import create_client, Client

def get_nfl_scoreboard() -> dict:
    nfl_scoreboard = client.get('/s/scoreboard?lang=en-US&region=US&tz=America%2FNew_York&ysp_redesign=1&ysp_platform=desktop&leagues=nfl&week=current&season=current')
    return nfl_scoreboard.json().get('service').get('scoreboard').get('games')

def parse_nfl_scoreboard_data(scoreboard: dict) -> dict:
    games = {}

    fields_to_extract = ["gameid", "start_time", "home_team_id", "away_team_id", "game_type", 
                         "winning_team_id", "week_number", "total_away_points", "total_home_points", "season"]
    
    for game in scoreboard.values():
        games[game.get('gameid')] = {key: game.get(key) for key in fields_to_extract}
    
    return games

def insert_to_supabase(scoreboard: dict):
    try:
        records = []
        for game in scoreboard.values():
            records.append(game)
        
        response = supabase.table('games').upsert(records).execute()
        print('Data inserted to supabase successfully!')

    except Exception as e:
        print(f'Error inserting to supabase: {e}')

if __name__ == '__main__':
    client = httpx.Client(base_url = 'https://api-secure.sports.yahoo.com/v1/editorial')
    if not os.getenv('DATABASE_URL') or not os.getenv('DATABASE_KEY'):
        print('Environment Secrets not fetched!')
    supabase: Client = create_client(os.getenv('DATABASE_URL'), os.getenv('DATABASE_KEY'))
    scoreboard = get_nfl_scoreboard()
    parsed_scoreboard = parse_nfl_scoreboard_data(scoreboard)
    try:
        insert_to_supabase(parsed_scoreboard)
    except Exception as e:
        print(f"Error: {e}")