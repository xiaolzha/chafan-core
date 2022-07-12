"""Update user model

Revision ID: 8c4461051c79
Revises: d81294903342
Create Date: 2021-01-01 13:22:33.406488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c4461051c79'
down_revision = 'd81294903342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site', sa.Column('upvote_answer_coin_deduction', sa.Integer(), server_default='2', nullable=False))
    op.add_column('user', sa.Column('sent_new_user_invitataions', sa.Integer(), server_default='0', nullable=False))
    op.drop_column('user', 'sent_invitataions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('sent_invitataions', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.drop_column('user', 'sent_new_user_invitataions')
    op.drop_column('site', 'upvote_answer_coin_deduction')
    # ### end Alembic commands ###
