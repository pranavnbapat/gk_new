"""Add history tables

Revision ID: c86725056ea4
Revises: 86dabfbf21c1
Create Date: 2025-06-10 21:56:07.406414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c86725056ea4'
down_revision: Union[str, None] = '86dabfbf21c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('auth_user_extend', 'uuid',
               existing_type=mysql.VARCHAR(length=36),
               nullable=False)
    op.alter_column('auth_user_extend', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text('1'))
    op.alter_column('auth_user_extend', 'is_staff',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('auth_user_extend', 'is_superuser',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('auth_user_extend', 'date_joined',
               existing_type=mysql.DATETIME(fsp=6),
               nullable=False)
    op.create_index(op.f('ix_auth_user_extend_contact_no'), 'auth_user_extend', ['contact_no'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_user_extend_contact_no'), table_name='auth_user_extend')
    op.alter_column('auth_user_extend', 'date_joined',
               existing_type=mysql.DATETIME(fsp=6),
               nullable=True)
    op.alter_column('auth_user_extend', 'is_superuser',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('auth_user_extend', 'is_staff',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('auth_user_extend', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text('1'))
    op.alter_column('auth_user_extend', 'uuid',
               existing_type=mysql.VARCHAR(length=36),
               nullable=True)
    # ### end Alembic commands ###
