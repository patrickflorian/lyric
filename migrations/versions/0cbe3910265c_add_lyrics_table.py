"""add lyrics table

Revision ID: 0cbe3910265c
Revises: a34d8b51d882
Create Date: 2019-11-06 16:01:44.903586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cbe3910265c'
down_revision = 'a34d8b51d882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lyric', sa.Column('public_id', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'lyric', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lyric', type_='unique')
    op.drop_column('lyric', 'public_id')
    # ### end Alembic commands ###