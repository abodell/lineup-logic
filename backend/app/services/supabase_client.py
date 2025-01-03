import os
from dotenv import load_dotenv
from supabase import create_client, Client

if not os.environ.get('DATABASE_URL') or not os.environ.get('DATABASE_KEY'):
    load_dotenv()
# Create the supabase client
supabase: Client = create_client(os.environ.get('DATABASE_URL'), os.environ.get('DATABASE_KEY'))