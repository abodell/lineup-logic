from fastapi import APIRouter, Depends
from app.schemas.auth import UserCredentials
from app.services.auth import register_user, login_user, logout_user
from app.services.supabase_client import get_supabase
from supabase._async.client import AsyncClient

router = APIRouter()

@router.post('/auth/register')
async def register(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Register a new user
    return await register_user(user, supabase)
    
@router.post('/auth/login')
async def login(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Login an existing user and return an auth token
    return await login_user(user, supabase)

@router.post('/auth/logout')
async def logout(supabase: AsyncClient = Depends(get_supabase)):
    # Logout the current user
    return await logout_user(supabase)