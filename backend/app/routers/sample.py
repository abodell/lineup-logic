from fastapi import APIRouter
from app.services.ai import analyze_fantasy_data

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/ai/analyze")
def analyze():
    result = analyze_fantasy_data({'test': 'data'})
    return result
