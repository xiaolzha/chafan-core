"""Add description format fields for question archive

Revision ID: 975224f8aced
Revises: 6d8ddfacf048
Create Date: 2021-06-21 22:04:12.958530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '975224f8aced'
down_revision = '6d8ddfacf048'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questionarchive', sa.Column('description_text', sa.String(), nullable=True))
    op.add_column('questionarchive', sa.Column('description_editor', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questionarchive', 'description_editor')
    op.drop_column('questionarchive', 'description_text')
    # ### end Alembic commands ###
