"""Add UUIDs

Revision ID: 45c3d27894ca
Revises: 13285c952687
Create Date: 2021-01-30 15:13:44.890454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45c3d27894ca'
down_revision = '13285c952687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_site_uuid'), 'site', ['uuid'], unique=True)
    op.add_column('topic', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_topic_uuid'), 'topic', ['uuid'], unique=True)
    op.add_column('user', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_user_uuid'), 'user', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_uuid'), table_name='user')
    op.drop_column('user', 'uuid')
    op.drop_index(op.f('ix_topic_uuid'), table_name='topic')
    op.drop_column('topic', 'uuid')
    op.drop_index(op.f('ix_site_uuid'), table_name='site')
    op.drop_column('site', 'uuid')
    # ### end Alembic commands ###
