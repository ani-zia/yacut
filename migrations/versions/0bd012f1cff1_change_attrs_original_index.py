"""change attrs original -index

Revision ID: 0bd012f1cff1
Revises: fd0b25f693df
Create Date: 2022-09-01 17:08:46.992876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bd012f1cff1'
down_revision = 'fd0b25f693df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_URL_map_original', table_name='URL_map')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_URL_map_original', 'URL_map', ['original'], unique=False)
    # ### end Alembic commands ###
