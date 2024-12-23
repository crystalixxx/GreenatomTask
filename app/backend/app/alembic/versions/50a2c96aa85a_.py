"""empty message

Revision ID: 50a2c96aa85a
Revises: c2141fc20a10
Create Date: 2024-11-02 01:15:05.770804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50a2c96aa85a'
down_revision: Union[str, None] = 'c2141fc20a10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'is_read')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('is_read', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
