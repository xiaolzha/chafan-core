"""Update user model

Revision ID: 78bb836eff0a
Revises: 25b463cbeb95
Create Date: 2021-01-09 18:19:57.416894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78bb836eff0a'
down_revision = '25b463cbeb95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###