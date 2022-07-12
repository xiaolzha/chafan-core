"""Update model

Revision ID: 25b463cbeb95
Revises: 831dfdf03a18
Create Date: 2021-01-09 10:37:32.455225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25b463cbeb95'
down_revision = '831dfdf03a18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('coinpayment_event_json_payee_id_key', 'coinpayment', type_='unique')
    op.create_unique_constraint(None, 'coinpayment', ['event_json', 'payee_id', 'payer_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'coinpayment', type_='unique')
    op.create_unique_constraint('coinpayment_event_json_payee_id_key', 'coinpayment', ['event_json', 'payee_id'])
    # ### end Alembic commands ###