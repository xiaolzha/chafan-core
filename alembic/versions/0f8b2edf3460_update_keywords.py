"""Update keywords

Revision ID: 0f8b2edf3460
Revises: 3142c63f83f5
Create Date: 2021-09-05 10:17:23.273317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0f8b2edf3460'
down_revision = '3142c63f83f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'keywords_extracted_at')
    op.add_column('article', sa.Column('keywords', sa.JSON(), nullable=True))
    op.add_column('articlecolumn', sa.Column('keywords', sa.JSON(), nullable=True))
    op.drop_column('question', 'keywords_extracted_at')
    op.add_column('site', sa.Column('keywords', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site', 'keywords')
    op.add_column('question', sa.Column('keywords_extracted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('articlecolumn', 'keywords')
    op.drop_column('article', 'keywords')
    op.add_column('answer', sa.Column('keywords_extracted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###