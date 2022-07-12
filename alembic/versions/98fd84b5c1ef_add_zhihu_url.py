"""Add zhihu_url

Revision ID: 98fd84b5c1ef
Revises: 055c3cdb6b04
Create Date: 2021-12-11 23:42:13.048758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98fd84b5c1ef'
down_revision = '055c3cdb6b04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zhihu_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'zhihu_url')
    # ### end Alembic commands ###
