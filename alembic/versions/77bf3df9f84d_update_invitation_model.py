"""Update invitation model

Revision ID: 77bf3df9f84d
Revises: 3081fd03a6fb
Create Date: 2021-01-11 16:51:00.692594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77bf3df9f84d'
down_revision = '3081fd03a6fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invitation', sa.Column('invitation_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invitation', 'invitation_link')
    # ### end Alembic commands ###