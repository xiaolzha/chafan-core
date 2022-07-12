"""Update user model

Revision ID: c26f33a78370
Revises: ae37fb780460
Create Date: 2021-01-05 22:44:14.553160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c26f33a78370'
down_revision = 'ae37fb780460'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar_url')
    # ### end Alembic commands ###
