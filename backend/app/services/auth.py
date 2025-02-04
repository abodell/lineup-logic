from fastapi import HTTPException, Depends
from supabase._async.client import AsyncClient
from backend.app.models.auth import UserCredentials
from app.services.supabase_client import get_supabase


async def register_user(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Register a new user
    try:
        response = supabase.auth.sign_up({
            'email': user.email,
            'password': user.password,
            'options': {
                'data': { 'first_name': user.first_name, 'last_name': user.last_name}
            }
        })
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def login_user(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Login an existing user and return an auth token
    try:
        response = supabase.auth.sign_in_with_password({
            'email': user.email,
            'password': user.password 
        })
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def logout_user(supabase: AsyncClient = Depends(get_supabase)):
    # Logout the current user
    try:
        response = supabase.auth.sign_out()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))