"""my_migration

Revision ID: 49adb5781c27
Revises: 00000000
Create Date: 2020-02-06 16:05:34.969280

"""

# revision identifiers, used by Alembic.
revision = '49adb5781c27'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.execute('''
    UPDATE user SET point_balance=5000 WHERE user_id=1;
    ''')

    op.execute('''
    ALTER TABLE user ADD COLUMN location varchar(36);
    ''')

    op.execute('''
    UPDATE ohm_assessment.user SET location='USA' WHERE user_id=2;
    ''')
    
    op.execute('''
    UPDATE user SET tier='Silver' WHERE user_id=3;
    ''')


def downgrade():
    op.execute("TRUNCATE TABLE user")
    op.execute("TRUNCATE TABLE rel_user")
    op.execute("TRUNCATE TABLE rel_user_multi")

