"""Drop unique constraint

Revision ID: c7a34a6d6ed4
Revises: 0bd012f1cff1
Create Date: 2022-09-01 17:15:10.931245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a34a6d6ed4'
down_revision = '0bd012f1cff1'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('ix_URL_map_original', 'URL_map')


def downgrade():
    op.create_index(op.f('ix_URL_map_original'), 'URL_map', ['original'], unique=False)
