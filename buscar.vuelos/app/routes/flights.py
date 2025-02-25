from fastapi import APIRouter
import datetime as dt
from typing import Optional
from typing import Any
import app.database.flights as crud

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID1
from pygination import paginate
from pygination.errors import PaginationError
from pygination.models import PageModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.dependencies import get_db
from app.models.schema.flights import Flights

router = APIRouter()

@router.get("/")
def search(
    page: int = 0,
    size: int = 50,
    origin: Optional[str] = None, 
    destination: Optional[str] = None,  
    date: Optional[dt.datetime]= None,
    db: Session = Depends(get_db),
    ) -> Any:
    flights = crud.search(
        date=date,
        destination=destination,
        origin=origin,
        db=db
    )
    page = paginate(flights, page, size)
    pages = PageModel[Flights].from_orm(page)

    return pages