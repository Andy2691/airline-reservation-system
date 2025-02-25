"""Creacion_de_llaves_foraneas_2

Revision ID: b70f7afd0d2a
Revises: 501cee7099c7
Create Date: 2025-02-24 18:01:02.699359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b70f7afd0d2a'
down_revision = '501cee7099c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
        "flight_f_key",
        "reservas_de_vuelos",
        "registro_de_vuelos",
        ["flight_code"],
        ["flight_code"],
        source_schema="flights",
        referent_schema="flights",
    )


def downgrade() -> None:
    op.drop_constraint(
        "user_f_key",
        "reservas_de_vuelos",
        schema="flights",
        type="foreignkey",
    )