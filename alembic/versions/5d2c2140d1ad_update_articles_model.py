"""Update articles model

Revision ID: 5d2c2140d1ad
Revises: a4e5d081e50a
Create Date: 2021-01-26 22:20:12.069539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5d2c2140d1ad'
down_revision = 'a4e5d081e50a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('body_draft', sa.String(), nullable=True))
    op.add_column('article', sa.Column('draft_saved_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('article', sa.Column('editor', sa.String(), server_default='wysiwyg', nullable=False))
    op.add_column('article', sa.Column('initial_published_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('article', sa.Column('is_deleted', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('article', sa.Column('math_enabled', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('article', sa.Column('source_format', sa.String(), server_default='markdown', nullable=False))
    op.alter_column('article', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.create_unique_constraint(None, 'articleupvotes', ['article_id', 'voter_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articleupvotes', type_='unique')
    op.alter_column('article', 'updated_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.drop_column('article', 'source_format')
    op.drop_column('article', 'math_enabled')
    op.drop_column('article', 'is_deleted')
    op.drop_column('article', 'initial_published_at')
    op.drop_column('article', 'editor')
    op.drop_column('article', 'draft_saved_at')
    op.drop_column('article', 'body_draft')
    # ### end Alembic commands ###
