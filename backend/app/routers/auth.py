from fastapi import APIRouter, Depends, HTTPException, Response
from backend.app.models.auth import UserCredentials
from app.services.supabase_client import get_supabase
from supabase._async.client import AsyncClient
import app.services.auth as AuthService
import json

router = APIRouter()

@router.post('/register')
async def register(user: UserCredentials, supabase: AsyncClient = Depends(get_supabase)):
    # Register a new user
    return await AuthService.register_user(user, supabase)
    
@router.post('/login')
async def login(user: UserCredentials, response: Response, supabase: AsyncClient = Depends(get_supabase)):
    # Login an existing user and return an auth token
    auth_response = await AuthService.login_user(user, supabase)
    if not auth_response or "error" in auth_response:
        raise HTTPException(status_code=400, detail = "Invalid Credentials")

    session = auth_response.session
    response.set_cookie(
        key="access_token",
        value=session.access_token,
        httponly=True,
        max_age=session.expires_in,
        path='/',
        secure=False,
        samesite='lax'
    )
    response.status_code = 200
    response.body = json.dumps({"message": "Authentication Successful"}).encode('utf-8')
    return response

@router.post('/logout')
async def logout(response: Response, supabase: AsyncClient = Depends(get_supabase)):
    # Logout the current user
    await AuthService.logout_user(supabase)
    response.delete_cookie('access_token')
    response.status_code = 200
    response.body = json.dumps({"message": "Logged Out"}).encode('utf-8')
    return response