"""seed admin account

Revision ID: 7f7be73bbd4f
Revises: 5233aeceab32
Create Date: 2022-03-29 18:31:39.709252

"""
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '7f7be73bbd4f'
down_revision = '5233aeceab32'
branch_labels = None
depends_on = None


def upgrade():
    users_table = table('users',
        column('id', Integer),
        column('email', String),
        column('first_name', String),
        column('last_name', String),
        column('mobile_number', String),
        column('password', String),
        column('role', String)
    )

    op.bulk_insert(users_table,
        [
            {'email': 'test_admin@mayari.io',
            'first_name': 'Test', 'last_name': 'Admin',
            'mobile_number': '09266283273',
            'password':'sha256$AsdkkAwjjAJ92cjk$47dd33c25f99d970eddce79bfb84210438199050837e3a3f6b686cbe806d4961',
            'role': 'admin'}
        ]
    )


def downgrade():
    pass
