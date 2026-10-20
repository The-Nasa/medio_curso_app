"""create availability

Revision ID: 0002_create_availability
Revises: 0001_create_users
"""

import sqlalchemy as sa

from alembic import op

revision = "0002_create_availability"
down_revision = "0001_create_users"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "availability",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("end_time", sa.Time(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        sa.Column("is_reserved", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_availability_date", "availability", ["date"])


def downgrade() -> None:
    op.drop_index("ix_availability_date", table_name="availability")
    op.drop_table("availability")
