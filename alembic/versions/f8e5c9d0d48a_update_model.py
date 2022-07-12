"""Update model

Revision ID: f8e5c9d0d48a
Revises: 0144c1da0fe6
Create Date: 2021-02-01 18:11:24.287115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e5c9d0d48a'
down_revision = '0144c1da0fe6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reward', sa.Column('refunded_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reward', 'refunded_at')
    # ### end Alembic commands ###
