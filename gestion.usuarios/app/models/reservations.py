import datetime as dt
from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text
from sqlalchemy.types import DateTime

DB_SCHEMA = "flights"

from app.database.conn import Base

class users(Base):
    __tablename__ = "users"
    __table_args__ = (
        {
            "schema": DB_SCHEMA,
            "comment": "Tabla que almacena los usuarios",
        },
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=text("uuid_generate_v1()"),
        comment="ID único de Usuario",
    )
    name = Column(
        String,
        nullable=False,
        comment="Nombre de usuario",
    )
    lastname = Column(
        String,
        nullable=False,
        comment="Apellido Usuario",
    )
    email = Column(
        String,
        nullable=False,
        comment="Correo Usuario",
    )
    