import logging
from typing import Optional
import datetime as dt
from sqlalchemy.orm import Query, Session
from app.models.flights import Flights


logger = logging.getLogger(__name__)
def search( 
    db: Session, 
    origin: Optional[str]= None,
    destination:Optional[str]= None,
    date: Optional[dt.datetime]= None,
    ) -> Query:

    query = db.query(Flights)
    logger.info("Searching FLIGHTS")
    if origin is not None:
        query = query.filter(Flights.origin == origin)
        logger.debug(f"Filtering by origin : {origin }")
    if destination is not None:
        query = query.filter(Flights.destination == destination)
        logger.debug(f"Filtering by origin : {origin }")
    if date is not None:
        query = query.filter(Flights.date == date)
        logger.debug(f"Filtering by origin : {origin }")

    logger.debug(f"Query: {query.statement}")

    return query