"""Add editor to comment

Revision ID: a2c4da7f3afc
Revises: 6a66054d75b6
Create Date: 2021-03-26 17:33:16.627088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2c4da7f3afc'
down_revision = '6a66054d75b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('body_html', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'body_html')
    # ### end Alembic commands ###
