"""Creacion_de_llaves_foraneas

Revision ID: 501cee7099c7
Revises: e1b6faa181eb
Create Date: 2025-02-24 17:25:06.721849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '501cee7099c7'
down_revision = 'e1b6faa181eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
        "user_f_key",
        "reservas_de_vuelos",
        "users",
        ["user_code"],
        ["id"],
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
