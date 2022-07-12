"""Add gif_avatar_url

Revision ID: 842e9e21589b
Revises: c07f2ab88c8b
Create Date: 2021-02-04 00:18:00.030211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842e9e21589b'
down_revision = 'c07f2ab88c8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gif_avatar_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'gif_avatar_url')
    # ### end Alembic commands ###