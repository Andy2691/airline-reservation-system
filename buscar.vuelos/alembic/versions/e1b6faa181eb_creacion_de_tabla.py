

"""Creacion_de_tabla

Revision ID: e1b6faa181eb
Revises: e9dd236fb0a2
Create Date: 2025-02-24 14:38:53.445260

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e1b6faa181eb'
down_revision = 'e9dd236fb0a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "registro_de_vuelos",
        sa.Column(
            "flight_code",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v1()"),
            nullable=False,
            comment="Codigo de Vuelo",
        ),
        sa.Column(
            "destination",
            sa.String(),
            nullable=True,
            comment="Destino",
        ),
        sa.Column(
            "origin",
            sa.String(),
            nullable=True,
            comment="Origen",
        ),
        sa.Column(
            "date",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Fecha",
        ),
        sa.PrimaryKeyConstraint("flight_code"),
        schema="flights",
    ),
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v1()"),
            nullable=False,
            comment="Identificacion Usuario",
        ),
        sa.Column(
            "name",
            sa.String(),
            nullable=True,
            comment="Nombre Usuario",
        ),
        sa.Column(
            "lastname",
            sa.String(),
            nullable=True,
            comment="Apellido Usuario",
        ),
        sa.Column(
            "email",
            sa.String(),
            nullable=True,
            comment="correo Usuario",
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="flights",
    ),   
    op.create_table(
        "reservas_de_vuelos",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v1()"),
            nullable=False,
            comment="ID único de la reserva",
        ),
        sa.Column(
            "user_code",
            sa.UUID(),
            nullable=True,
            comment="ID del usuario que realiza la reserva",
        ),
        sa.Column(
            "flight_code",
            sa.UUID(),
            nullable=True,
            comment="Código del vuelo reservado",
        ),
        sa.Column(
            "seat_number",
            sa.String(),
            nullable=True,
            comment="Número de asiento asignado",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=True,
            comment="Fecha y hora de creación de la reserva",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        schema="flights",

)



def downgrade() -> None:
    op.drop_table("registro_de_vuelos", schema="flights")
    

