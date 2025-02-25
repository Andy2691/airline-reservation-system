"""Creacio_de_esquema

Revision ID: e9dd236fb0a2
Revises: 
Create Date: 2025-02-24 14:28:17.589623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9dd236fb0a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('create EXTENSION IF NOT exists "uuid-ossp"')
    op.execute("create schema flights")
   


def downgrade() -> None:
    op.execute('drop EXTENSION "uuid-ossp"')
    op.execute("drop schema flights")
   