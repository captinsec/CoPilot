"""Add timestamp to artifact table

Revision ID: 1ec08862d786
Revises: 26d24321c4c5
Create Date: 2023-07-24 14:47:39.209785

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1ec08862d786"
down_revision = "26d24321c4c5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("artifact", schema=None) as batch_op:
        batch_op.add_column(sa.Column("timestamp", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("artifact", schema=None) as batch_op:
        batch_op.drop_column("timestamp")

    # ### end Alembic commands ###