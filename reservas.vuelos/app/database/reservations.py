from sqlalchemy.orm import Session, Query
from uuid import uuid4
from app.models.schema.reservations import ReservationCreate
from app.models.reservations import Reservation
from typing import Optional, Any
from pydantic import UUID4
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def create_reservation(db: Session, reservation: ReservationCreate):
    """
    Crea una nueva reserva en la base de datos.
    """
    new_reservation = Reservation(
        id=uuid4(),
        user_code=reservation.user_id,
        flight_code=reservation.flight_id,
        seat_number=reservation.seat_number,
    
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation

def get_reservation_by_id(db: Session, reservation_id):
    """
    Obtiene una reserva por su ID.
    """
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()



def list_reservations(db: Session, user_id=None, flight_id=None):
    """
    Lista reservas con filtros opcionales.
    """
    query = db.query(Reservation)
    if user_id:
        query = query.filter(Reservation.user_id == user_id)
    if flight_id:
        query = query.filter(Reservation.flight_id == flight_id)
    
    return query.all()

def search( 
    db: Session, 
    user_id: Optional[UUID4] = None, 
    flight_id: Optional[UUID4] = None,  
    ) -> Query:

    query = db.query(Reservation)
    logger.info("Searching FLIGHTS")
    if user_id is not None:
        query = query.filter(Reservation.user_code == user_id)
        logger.debug(f"Filtering by user_code: {user_id }")
    if flight_id is not None:
        query = query.filter(Reservation.flight_code == flight_id)
        logger.debug(f"Filtering by flight_code : {flight_id }")
    

    logger.debug(f"Query: {query.statement}")

    return query


def cancel_reservation(db: Session, reservation_id):
    """
    Cancela una reserva por ID.
    """
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        return False
    
    reservation.status = "cancelled"
    db.commit()
    return True
