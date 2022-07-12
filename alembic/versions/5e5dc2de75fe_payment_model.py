"""Payment model

Revision ID: 5e5dc2de75fe
Revises: 6aefea467152
Create Date: 2020-12-26 23:50:55.571444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e5dc2de75fe'
down_revision = '6aefea467152'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coindeposit', sa.Column('ref_id', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'coindeposit', ['ref_id'])
    op.add_column('coinpayment', sa.Column('ref_id', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'coinpayment', ['ref_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'coinpayment', type_='unique')
    op.drop_column('coinpayment', 'ref_id')
    op.drop_constraint(None, 'coindeposit', type_='unique')
    op.drop_column('coindeposit', 'ref_id')
    # ### end Alembic commands ###