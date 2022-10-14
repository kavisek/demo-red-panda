"""baseline

Revision ID: f32c28b4bc0b
Revises: 
Create Date: 2022-10-13 09:29:43.149516

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, Integer, String, DateTime

# revision identifiers, used by Alembic.
revision = "f32c28b4bc0b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create schema "users"')
    op.create_table(
        "events",
        Column("id", Integer, primary_key=True),
        Column("first_name", String(50), nullable=False),
        Column("last_name", String(50), nullable=False),
        Column("email", String(255), nullable=False),
        Column("status", String(255), nullable=False),
        Column("created_at", DateTime, nullable=False),
        Column("updated_at", DateTime, nullable=False),
        schema="users",
    )
    pass


def downgrade():
    op.drop_table("events", schema="users")
    op.execute('drop schema "users" cascade')
    pass
