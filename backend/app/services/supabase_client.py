import os
from dotenv import load_dotenv
from supabase._async.client import AsyncClient as AsyncClient, create_client as async_create_client

if not os.environ.get('DATABASE_URL') or not os.environ.get('DATABASE_KEY'):
    load_dotenv()
async def get_supabase() -> AsyncClient:
    return await async_create_client(os.environ.get('DATABASE_URL'), os.environ.get('DATABASE_KEY'))