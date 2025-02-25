import datetime as dt
from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text
from sqlalchemy.types import DateTime

DB_SCHEMA = "flights"

from app.database.conn import Base

class Reservation(Base):
    __tablename__ = "reservas_de_vuelos"
    __table_args__ = (
        {
            "schema": DB_SCHEMA,
            "comment": "Tabla que almacena las reservas de vuelos",
        },
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=text("uuid_generate_v4()"),
        comment="ID único de la reserva",
    )
    user_code = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment="ID del usuario que realiza la reserva",
    )
    flight_code = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment="Código del vuelo reservado",
    )
    seat_number = Column(
        String,
        nullable=False,
        comment="Número de asiento asignado",
    )
    created_at = Column(
        DateTime(timezone=True),
        default=dt.datetime.utcnow,
        server_default=text("NOW()"),
        nullable=False,
        comment="Fecha y hora de creación de la reserva",
    )
