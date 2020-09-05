"""empty message

Revision ID: 29627ba45bd0
Revises: a00571a7d924
Create Date: 2020-09-03 20:38:46.828427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29627ba45bd0'
down_revision = 'a00571a7d924'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('cover_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'cover_image')
    # ### end Alembic commands ###