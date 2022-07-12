"""Update model

Revision ID: fd40a9df4c39
Revises: c26f33a78370
Create Date: 2021-01-09 02:54:53.543753

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fd40a9df4c39'
down_revision = 'c26f33a78370'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_blog_id_fkey', 'comment', type_='foreignkey')
    op.drop_index('ix_blog_author_id', table_name='blog')
    op.drop_index('ix_blog_id', table_name='blog')
    op.drop_index('ix_blog_site_id', table_name='blog')
    op.drop_table('blog')
    op.add_column('activity', sa.Column('event_json', sa.String(), nullable=True))
    op.alter_column('activity', 'content_json',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index('ix_comment_blog_id', table_name='comment')
    op.drop_column('comment', 'blog_id')
    op.add_column('notification', sa.Column('event_json', sa.String(), nullable=True))
    op.drop_column('notification', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('notification', 'event_json')
    op.add_column('comment', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comment_blog_id_fkey', 'comment', 'blog', ['blog_id'], ['id'])
    op.create_index('ix_comment_blog_id', 'comment', ['blog_id'], unique=False)
    op.alter_column('activity', 'content_json',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('activity', 'event_json')
    op.create_table('blog',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('site_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('topic_ids', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('like_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='blog_author_id_fkey'),
    sa.ForeignKeyConstraint(['site_id'], ['site.id'], name='blog_site_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blog_pkey')
    )
    op.create_index('ix_blog_site_id', 'blog', ['site_id'], unique=False)
    op.create_index('ix_blog_id', 'blog', ['id'], unique=False)
    op.create_index('ix_blog_author_id', 'blog', ['author_id'], unique=False)
    # ### end Alembic commands ###