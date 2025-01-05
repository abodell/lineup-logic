import httpx
import os
from supabase import create_client, Client

def get_sleeper_data():
    player_data = client.get('/players/nfl')
    return player_data.json()

def insert_to_supabase(data):
    try:
        # Prepare data for bulk upsert
        records = []
        for player_id, player_data in data.items():
            record = {
                "player_id": player_data.get("player_id"),
                "first_name": player_data.get("first_name"),
                "last_name": player_data.get("last_name"),
                "team": player_data.get("team"),
                "position": player_data.get("position"),
                "fantasy_positions": player_data.get("fantasy_positions", []),
                "number": player_data.get("number"),
                "age": player_data.get("age"),
                "height": player_data.get("height"),
                "weight": player_data.get("weight"),
                "years_exp": player_data.get("years_exp"),
                "college": player_data.get("college"),
                "depth_chart_position": player_data.get("depth_chart_position"),
                "depth_chart_order": player_data.get("depth_chart_order"),
                "status": player_data.get("status"),
                "injury_status": player_data.get("injury_status"),
                "injury_start_date": player_data.get("injury_start_date"),
                "practice_participation": player_data.get("practice_participation"),
                "search_first_name": player_data.get("search_first_name"),
                "search_last_name": player_data.get("search_last_name"),
                "search_full_name": player_data.get("search_full_name"),
                "search_rank": player_data.get("search_rank"),
                "rotoworld_id": player_data.get("rotoworld_id"),
                "rotowire_id": player_data.get("rotowire_id"),
                "yahoo_id": player_data.get("yahoo_id"),
                "espn_id": player_data.get("espn_id"),
                "fantasy_data_id": player_data.get("fantasy_data_id"),
                "stats_id": player_data.get("stats_id"),
                "sportradar_id": player_data.get("sportradar_id"),
                "hashtag": player_data.get("hashtag"),
                "sport": player_data.get("sport"),
                "birth_country": player_data.get("birth_country")
            }
            records.append(record)

        # Perform bulk upsert
        response = supabase.table("players").upsert(records).execute()
        print(response)
        if response.status_code != 201:
            print(f"Failed to upsert records: {response.data}")
        else:
            print(f"Successfully upserted {len(records)} records")
    except Exception as e:
        print(f"Error during bulk upsert: {e}")

if __name__ == "__main__":
    client = httpx.Client(base_url='https://api.sleeper.app/v1')
    if not os.getenv('DATABASE_URL') or not os.getenv('DATABASE_KEY'):
        print('Environment Secrets not fetched!')
    supabase: Client = create_client(os.getenv('DATABASE_URL'), os.getenv('DATABASE_KEY'))
    try:
        data = get_sleeper_data()
        insert_to_supabase(data)
    except Exception as e:
        print(f'Error: {e}')