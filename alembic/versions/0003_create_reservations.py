"""create reservations

Revision ID: 0003_create_reservations
Revises: 0002_create_availability
"""
import sqlalchemy as sa

from alembic import op

revision = "0003_create_reservations"
down_revision = "0002_create_availability"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "reservations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column(
            "availability_id", sa.Integer(), sa.ForeignKey("availability.id"), nullable=False
        ),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="confirmed"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column("cancelled_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_reservations_user_id", "reservations", ["user_id"])
    op.create_index("ix_reservations_availability_id", "reservations", ["availability_id"])


def downgrade() -> None:
    op.drop_index("ix_reservations_availability_id", table_name="reservations")
    op.drop_index("ix_reservations_user_id", table_name="reservations")
    op.drop_table("reservations")
