import datetime as dt
from uuid import uuid1

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text
from sqlalchemy.types import Date, DateTime

DB_SCHEMA = "flights"

from app.database.conn import Base

class Flights(Base):
    __tablename__ = "registro_de_vuelos"
    __table_args__ = (
        {
            "schema": DB_SCHEMA,
            "comment": "Tabla que almacena los vuelos",
        },
    )
    flight_code = Column(
        String,
        primary_key=True,
        nullable=True,
        comment="Codigo del vuelo",
    )
    date = Column(
        DateTime(timezone=True),
        default=dt.datetime.utcnow,
        server_default=text("NOW()"),
        nullable=False,
        comment="TimesTamp del vuelo",
    )
    origin = Column(
        String,
        nullable=True,
        comment="Origen",
    )
    destination = Column(
        String,
        nullable=True,
        comment="destino",
    )