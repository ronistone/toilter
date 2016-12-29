"""empty message

Revision ID: ffa0556aa016
Revises: a3e05acff3a7
Create Date: 2016-11-24 21:57:34.018458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa0556aa016'
down_revision = 'a3e05acff3a7'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('second', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'second')
    ### end Alembic commands ###