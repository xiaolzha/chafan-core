"""Add UUIDs

Revision ID: 36266ab34428
Revises: 45c3d27894ca
Create Date: 2021-01-30 15:26:53.048052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36266ab34428'
down_revision = '45c3d27894ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_answer_uuid'), 'answer', ['uuid'], unique=True)
    op.add_column('article', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_article_uuid'), 'article', ['uuid'], unique=True)
    op.add_column('articlecolumn', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_articlecolumn_uuid'), 'articlecolumn', ['uuid'], unique=True)
    op.add_column('comment', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_comment_uuid'), 'comment', ['uuid'], unique=True)
    op.add_column('question', sa.Column('uuid', sa.CHAR(length=20), nullable=True))
    op.create_index(op.f('ix_question_uuid'), 'question', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_uuid'), table_name='question')
    op.drop_column('question', 'uuid')
    op.drop_index(op.f('ix_comment_uuid'), table_name='comment')
    op.drop_column('comment', 'uuid')
    op.drop_index(op.f('ix_articlecolumn_uuid'), table_name='articlecolumn')
    op.drop_column('articlecolumn', 'uuid')
    op.drop_index(op.f('ix_article_uuid'), table_name='article')
    op.drop_column('article', 'uuid')
    op.drop_index(op.f('ix_answer_uuid'), table_name='answer')
    op.drop_column('answer', 'uuid')
    # ### end Alembic commands ###