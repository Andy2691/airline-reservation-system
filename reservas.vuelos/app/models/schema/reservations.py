from pydantic import BaseModel, UUID1, UUID4
from typing import Optional

class ReservationCreate(BaseModel):
    user_id: UUID1
    flight_id: UUID1
    seat_number: str

class ReservationResponse(BaseModel):
    id: UUID4
    user_id: UUID1
    flight_id: UUID1
    seat_number: str

    class Config:
        from_attributes = True
