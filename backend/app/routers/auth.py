from fastapi import APIRouter
from app.schemas.auth import UserCredentials
from app.services.auth import register_user, login_user, logout_user

router = APIRouter()

@router.post('/auth/register')
async def register(user: UserCredentials):
    # Register a new user
    return await register_user(user)
    
@router.post('/auth/login')
async def login(user: UserCredentials):
    # Login an existing user and return an auth token
    return await login_user(user)

@router.post('/auth/logout')
async def logout():
    # Logout the current user
    return await logout_user()