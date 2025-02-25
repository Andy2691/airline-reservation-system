from sqlalchemy.orm import Session, Query
from uuid import uuid4, uuid1
from app.models.schema.users import UserCreate
from app.models.reservations import users
from typing import Optional, Any
from pydantic import UUID4
from typing import Optional
import logging

logger = logging.getLogger(__name__)


def create_user(db: Session, user: UserCreate):
    """
    Crea una nueva reserva en la base de datos.
    """
    new_user = users(
        id=uuid1(),
        name=user.name,
        lastname=user.lastname,
        email=user.email,
    
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def search( 
    db: Session, 
    name: Optional[str] = None, 
    lastname: Optional[str] = None,  
    ) -> Query:

    query = db.query(users)
    logger.info("Searching FLIGHTS")
    if name is not None:
        query = query.filter(users.name == name)
        logger.debug(f"Filtering by name: {name }")
    if lastname is not None:
        query = query.filter(users.lastname == lastname)
        logger.debug(f"Filtering by lastname : {lastname }")
    

    logger.debug(f"Query: {query.statement}")

    return query

