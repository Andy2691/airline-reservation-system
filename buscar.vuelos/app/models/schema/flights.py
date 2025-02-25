import datetime as dt
from typing import List, Optional

from pydantic import UUID1, BaseModel


class Flights(BaseModel):

    date: dt.datetime
    flight_code: Optional[str]
    origin: Optional[str]
    destination: Optional[str]

    class Config:
        orm_mode = True


    