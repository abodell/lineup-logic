import os
from dotenv import load_dotenv
from supabase import create_client, Client
from supabase._async.client import AsyncClient as AsyncClient, create_client as async_create_client

if not os.environ.get('DATABASE_URL') or not os.environ.get('DATABASE_KEY'):
    load_dotenv()
# Create the async supabase client
supabase: Client = create_client(os.environ.get('DATABASE_URL'), os.environ.get('DATABASE_KEY'))
async def create_supabase() -> AsyncClient:
    return await async_create_client(os.environ.get('DATABASE_URL'), os.environ.get('DATABASE_KEY'))