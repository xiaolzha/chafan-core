"""Add sub-topic

Revision ID: 69f40011f79e
Revises: b1c1a85fb152
Create Date: 2021-01-29 21:39:19.213544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69f40011f79e'
down_revision = 'b1c1a85fb152'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('parent_topic_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_topic_parent_topic_id'), 'topic', ['parent_topic_id'], unique=False)
    op.create_foreign_key(None, 'topic', 'topic', ['parent_topic_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'topic', type_='foreignkey')
    op.drop_index(op.f('ix_topic_parent_topic_id'), table_name='topic')
    op.drop_column('topic', 'parent_topic_id')
    # ### end Alembic commands ###
