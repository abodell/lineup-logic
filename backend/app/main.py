from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, sleeper, espn, yahoo

app = FastAPI(root_path='/api')

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?:\/\/localhost(:\d+)?",  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix='/auth')
app.include_router(sleeper.router)
app.include_router(espn.router)
app.include_router(yahoo.router)

@app.get('/')
def home():
    return {'message': 'hello'}