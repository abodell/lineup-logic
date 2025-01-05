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
                "player_id": player_data["player_id"],
                "first_name": player_data["first_name"],
                "last_name": player_data["last_name"],
                "team": player_data["team"],
                "position": player_data["position"],
                "fantasy_positions": player_data["fantasy_positions"],
                "number": player_data["number"],
                "age": player_data["age"],
                "height": player_data["height"],
                "weight": player_data["weight"],
                "years_exp": player_data["years_exp"],
                "college": player_data["college"],
                "depth_chart_position": player_data["depth_chart_position"],
                "depth_chart_order": player_data["depth_chart_order"],
                "status": player_data["status"],
                "injury_status": player_data["injury_status"],
                "injury_start_date": player_data["injury_start_date"],
                "practice_participation": player_data["practice_participation"],
                "search_first_name": player_data["search_first_name"],
                "search_last_name": player_data["search_last_name"],
                "search_full_name": player_data["search_full_name"],
                "search_rank": player_data["search_rank"],
                "rotoworld_id": player_data["rotoworld_id"],
                "rotowire_id": player_data["rotowire_id"],
                "yahoo_id": player_data["yahoo_id"],
                "espn_id": player_data["espn_id"],
                "fantasy_data_id": player_data["fantasy_data_id"],
                "stats_id": player_data["stats_id"],
                "sportradar_id": player_data["sportradar_id"],
                "hashtag": player_data["hashtag"],
                "sport": player_data["sport"],
                "birth_country": player_data["birth_country"]
            }
            print(record['number'])
            records.append(record)

        # Perform bulk upsert
        response = supabase.table("players").upsert(records).execute()
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