"""Update invitation model

Revision ID: 6a3707257d81
Revises: 78bb836eff0a
Create Date: 2021-01-10 19:54:52.202751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a3707257d81'
down_revision = '78bb836eff0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invitation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('inviter_id', sa.Integer(), nullable=False),
    sa.Column('invited_email', sa.String(), nullable=True),
    sa.Column('invited_user_id', sa.Integer(), nullable=True),
    sa.Column('invited_to_site_id', sa.Integer(), nullable=True),
    sa.Column('is_sent', sa.Boolean(), server_default='false', nullable=False),
    sa.ForeignKeyConstraint(['invited_to_site_id'], ['site.id'], ),
    sa.ForeignKeyConstraint(['invited_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['inviter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invitation')
    # ### end Alembic commands ###
