from fastapi import APIRouter, Depends, HTTPException, status
import datetime as dt
from typing import Optional, Any
import app.database.users as crud

from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.schema.users import UserCreate, UserResponse
from pydantic import UUID4
from pygination import paginate
from pygination.models import PageModel

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Crea un nuevo Usuario.
    """
    new_user = crud.create_user(db=db, user=user)
    if not new_user:
        raise HTTPException(status_code=400, detail="No se pudo crear el Usuario")
    reserva = UserResponse(
        id= new_user.id,
        name=  new_user.name,
        lastname= new_user.lastname,
        email= new_user.email
    )
    diccionario = reserva.dict()
    
    return diccionario


@router.get("/")
def search(
    page: int = 0,
    size: int = 50,
    name: Optional[str] = None, 
    lastname: Optional[str] = None,  
    db: Session = Depends(get_db),
    ) -> Any:
    reservas = crud.search(
        name = name,
        lastname =lastname,
        db=db
    )
    page = paginate(reservas, page, size)
    pages = PageModel[UserResponse].from_orm(page)

    return pages

