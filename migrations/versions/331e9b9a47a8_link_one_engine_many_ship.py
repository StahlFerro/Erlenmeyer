"""Link_One_Engine_Many_Ship

Revision ID: 331e9b9a47a8
Revises: 7c1fe1050867
Create Date: 2018-11-20 21:55:16.175271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331e9b9a47a8'
down_revision = '7c1fe1050867'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ship', sa.Column('engine_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ship', 'engine', ['engine_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ship', type_='foreignkey')
    op.drop_column('ship', 'engine_id')
    # ### end Alembic commands ###
