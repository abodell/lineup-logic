from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCredentials(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class CurrentUser(BaseModel):
    email: EmailStr
    id: str
    first_name: str
    last_name: str
    created_at: datetime
