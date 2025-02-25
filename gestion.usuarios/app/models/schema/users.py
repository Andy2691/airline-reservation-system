from pydantic import BaseModel, UUID1, UUID4
from typing import Optional

class UserCreate(BaseModel):
    name: str
    lastname: str
    email: str

class UserResponse(BaseModel):
    id: UUID1
    name: str
    lastname: str
    email: str

    class Config:
        from_attributes = True
