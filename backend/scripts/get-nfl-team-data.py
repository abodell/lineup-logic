import httpx
import os
from supabase import create_client, Client

def get_nfl_teams_data() -> dict:
    nfl_teams_data = client.get('/sports.league.standings;alias=mini_standings;combineGroups=;conference=;count=100;division=;league=nfl;leagueSeason=standings')
    return nfl_teams_data.json()

def parse_teams_data(data: dict) -> dict:
    teams = {}

    fields_to_extract = ["team_id", "full_name", "abbr", "conference_abbr", "conference_id", "division", "division_id", "group_position"]

    for id in data.get('teams'):
        teams[id] = []
        extracted_data = {key: data.get('teams').get(id).get(key) for key in fields_to_extract}
        teams[id] = extracted_data
    
    for id in data.get('teambye_week'):
        teams[id]['teambye_week'] = data.get('teambye_week').get(id)
    
    for id in data.get('teamteam_standing'):
        teams[id]['team_record'] = data.get('teamteam_standing').get(id).get('team_record').get('display')
        teams[id]['conference_record'] = data.get('teamteam_standing').get(id).get('team_conference_record').get('display')
        teams[id]['division_record'] = data.get('teamteam_standing').get(id).get('team_division_record').get('display')
        teams[id]['season'] = data.get('teamteam_standing').get(id).get('season')
        teams[id]['playoff_ranking'] = data.get('teamteam_standing').get(id).get('wildcard_standings').get('position')

    return teams

def insert_to_supabase(team_data: dict):
    try:
        records = []
        for team_id, team_data in team_data.items():
            record = {
                "team_id": team_data.get('team_id'),
                "season": team_data.get('season'),
                "team_name": team_data.get('full_name'),
                "divison_name": f"{team_data.get('conference_abbr')} {team_data.get('division')}",
                "conference_name": team_data.get('conference_abbr'),
                "division_id": team_data.get('division_id'),
                "conference_id": team_data.get('conference_id'),
                "division_ranking": team_data.get('group_position'),
                "bye_week": team_data.get('teambye_week'),
                "conference_record": team_data.get('conference_record'),
                "division_record": team_data.get('division_record'),
                "team_record": team_data.get('team_record'),
                "playoff_ranking": int(team_data.get('playoff_ranking')),
                "team_abbr": team_data.get('abbr')
            }

            records.append(record)
        
        response = supabase.table('teams').upsert(records).execute()
        print('Data Inserted to Supabase Successfully!')
    except Exception as e:
        print(f"Error during bulk upsert: {e}")


if __name__ == "__main__":
    client = httpx.Client(base_url = 'https://sports.yahoo.com/site/api/resource')
    if not os.getenv('DATABASE_URL') or not os.getenv('DATABASE_KEY'):
        print('Environment Secrets not fetched!')
    supabase: Client = create_client('https://eovpidzqprlmiupgzkfe.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvdnBpZHpxcHJsbWl1cGd6a2ZlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzU4NjYzMTksImV4cCI6MjA1MTQ0MjMxOX0.QAc9Et4WivQea4Iy6vccNuwyd6HU7_zZfVvgHucnSuU')
    data = get_nfl_teams_data()
    parsed_data = parse_teams_data(data)
    try:
        insert_to_supabase(parsed_data)
    except Exception as e:
        print(f"Error: {e}")
