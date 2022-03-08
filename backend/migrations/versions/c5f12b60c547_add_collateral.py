"""add collateral

Revision ID: c5f12b60c547
Revises: 
Create Date: 2022-02-15 01:02:38.552172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f12b60c547'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loans', sa.Column('collateral', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('loans', 'collateral')
    # ### end Alembic commands ###