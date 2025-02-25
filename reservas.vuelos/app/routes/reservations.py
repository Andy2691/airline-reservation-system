from fastapi import APIRouter, Depends, HTTPException, status
import datetime as dt
from typing import Optional, Any
import app.database.reservations as crud

from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.schema.reservations import ReservationCreate, ReservationResponse
from pydantic import UUID4
from pygination import paginate
from pygination.models import PageModel

router = APIRouter()

@router.post("/", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Crea una nueva reserva de vuelo.
    """
    new_reservation = crud.create_reservation(db=db, reservation=reservation)
    if not new_reservation:
        raise HTTPException(status_code=400, detail="No se pudo crear la reserva")
    reserva = ReservationResponse(
        id= new_reservation.id,
        user_id = new_reservation.user_code,
        flight_id = new_reservation.flight_code,
        seat_number = new_reservation.seat_number
    )
    diccionario = reserva.dict()
    
    return diccionario

@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(
    reservation_id: UUID4,
    db: Session = Depends(get_db),
) -> Any:
    """
    Obtiene una reserva específica por ID.
    """
    reservation = crud.get_reservation_by_id(db=db, reservation_id=reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    reserva = ReservationResponse(
        id= reservation.id,
        user_id = reservation.user_code,
        flight_id = reservation.flight_code,
        seat_number = reservation.seat_number
    )
    diccionario = reserva.dict()
    return diccionario


@router.get("/")
def search(
    page: int = 0,
    size: int = 50,
    user_id: Optional[UUID4] = None, 
    flight_id: Optional[UUID4] = None,  
    db: Session = Depends(get_db),
    ) -> Any:
    reservas = crud.search(
        user_id=user_id,
        flight_id=flight_id,
        db=db
    )
    page = paginate(reservas, page, size)
    pages = PageModel[ReservationResponse].from_orm(page)

    return pages


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(
    reservation_id: UUID4,
    db: Session = Depends(get_db),
) -> None:
    """
    Cancela una reserva por ID.
    """
    success = crud.cancel_reservation(db=db, reservation_id=reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reserva no encontrada o ya cancelada")
