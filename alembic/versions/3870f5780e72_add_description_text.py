"""Add description_text

Revision ID: 3870f5780e72
Revises: 05c3a952ea62
Create Date: 2021-03-23 18:20:48.595673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3870f5780e72'
down_revision = '05c3a952ea62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('description_text', sa.String(), nullable=True))
    op.add_column('submission', sa.Column('description_text', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'description_text')
    op.drop_column('question', 'description_text')
    # ### end Alembic commands ###
