from fastapi import HTTPException
from schemas.auth import UserCredentials
from app.services.supabase_client import supabase


async def register_user(user: UserCredentials):
    # Register a new user
    try:
        response = supabase.auth.sign_up({
            'email': user.email,
            'password': user.password
        })
        return {'message': 'User signed up successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def login_user(user: UserCredentials):
    # Login an existing user and return an auth token
    try:
        response = supabase.auth.sign_in_with_password({
            'email': user.email,
            'password': user.password        
        })
        return {'message:': 'User logged in successfully!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def logout_user():
    # Logout the current user
    try:
        response = supabase.auth.sign_out()
        return {'message': 'User signed out!', 'data': response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))