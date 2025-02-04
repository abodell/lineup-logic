from fastapi import HTTPException, Depends
from supabase._async.client import AsyncClient
from app.schemas.auth import UserCredentials
from app.services.supabase_client import get_supabase


async def register_user(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Register a new user
    try:
        response = supabase.auth.sign_up({
            'email': user.email,
            'password': user.password
        })
        return {'message': 'User signed up successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def login_user(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Login an existing user and return an auth token
    try:
        response = supabase.auth.sign_in_with_password({
            'email': user.email,
            'password': user.password        
        })
        return {'message:': 'User logged in successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def logout_user(supabase: AsyncClient = Depends(get_supabase)):
    # Logout the current user
    try:
        response = supabase.auth.sign_out()
        return {'message': 'User signed out!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))