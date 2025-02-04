from fastapi import HTTPException, Depends, Request
from supabase._async.client import AsyncClient
from app.models.auth import UserCredentials
from app.services.supabase_client import get_supabase


async def register_user(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Register a new user
    try:
        response = await supabase.auth.sign_up({
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
        response = await supabase.auth.sign_in_with_password({
            'email': user.email,
            'password': user.password 
        })
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def logout_user(supabase: AsyncClient = Depends(get_supabase)):
    # Logout the current user
    try:
        response = await supabase.auth.sign_out()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def get_current_user(request: Request, supabase: AsyncClient = Depends(get_supabase)):
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    
    user = await supabase.auth.get_user(access_token)
    if not user:
        raise HTTPException(status_code=401, detail = "Invalid Token")
    
    return user.user