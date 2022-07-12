"""Add feedback status field

Revision ID: 3142c63f83f5
Revises: f3925b9ee72e
Create Date: 2021-08-27 21:53:15.458100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3142c63f83f5'
down_revision = 'f3925b9ee72e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('status', sa.String(), server_default='sent', nullable=False))
    op.drop_column('invitation', 'personal_relation')
    op.drop_column('invitation', 'invited_email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invitation', sa.Column('invited_email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('invitation', sa.Column('personal_relation', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('feedback', 'status')
    # ### end Alembic commands ###
