"""add language to posts

Revision ID: 5261fee6ea99
Revises: 53daa63fb4c8
Create Date: 2020-07-26 09:43:49.409697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5261fee6ea99'
down_revision = '53daa63fb4c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
