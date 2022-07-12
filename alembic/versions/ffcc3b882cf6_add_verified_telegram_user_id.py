"""Add verified_telegram_user_id

Revision ID: ffcc3b882cf6
Revises: 1e95c68901bb
Create Date: 2021-06-05 00:00:56.871712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffcc3b882cf6'
down_revision = '1e95c68901bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('verified_telegram_user_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'verified_telegram_user_id')
    # ### end Alembic commands ###