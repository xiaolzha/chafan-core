"""Add comment upvotes

Revision ID: 2668718cdb60
Revises: d706a80ce0a8
Create Date: 2021-02-13 09:59:04.497004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2668718cdb60'
down_revision = 'd706a80ce0a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commentupvotes',
    sa.Column('cancelled', sa.Boolean(), server_default='false', nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('comment_id', 'voter_id'),
    sa.UniqueConstraint('comment_id', 'voter_id')
    )
    op.create_index(op.f('ix_commentupvotes_comment_id'), 'commentupvotes', ['comment_id'], unique=False)
    op.create_index(op.f('ix_commentupvotes_voter_id'), 'commentupvotes', ['voter_id'], unique=False)
    op.add_column('comment', sa.Column('upvotes_count', sa.Integer(), server_default='0', nullable=False))
    op.create_unique_constraint(None, 'submissionupvotes', ['submission_id', 'voter_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'submissionupvotes', type_='unique')
    op.drop_column('comment', 'upvotes_count')
    op.drop_index(op.f('ix_commentupvotes_voter_id'), table_name='commentupvotes')
    op.drop_index(op.f('ix_commentupvotes_comment_id'), table_name='commentupvotes')
    op.drop_table('commentupvotes')
    # ### end Alembic commands ###
