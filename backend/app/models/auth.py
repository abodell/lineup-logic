from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCredentials(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


