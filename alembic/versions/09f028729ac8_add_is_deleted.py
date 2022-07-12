"""Add is_deleted

Revision ID: 09f028729ac8
Revises: e476333cd0b1
Create Date: 2021-01-17 01:47:43.985225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09f028729ac8'
down_revision = 'e476333cd0b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'activity', 'site', ['site_id'], ['id'])
    op.add_column('answer', sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False))
    op.alter_column('answer', 'body',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'body',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('answer', 'is_deleted')
    op.drop_constraint(None, 'activity', type_='foreignkey')
    # ### end Alembic commands ###
