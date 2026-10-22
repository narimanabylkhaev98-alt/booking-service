from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict 

from app.models import UserRole



class UserCreate(BaseModel):
    email: EmailStr
    password: str
    user_name: str | None = None
    business_name: str | None = None 


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    email: str
    role: UserRole
    user_name: str | None = None
    business_name: str | None = None
    created_at: datetime 
    
