"""employees and departments tables

Revision ID: 418a01e7cf07
Revises: 
Create Date: 2020-02-28 12:11:44.012770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418a01e7cf07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_name'), 'department', ['name'], unique=False)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_last_name'), 'employee', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_last_name'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_department_name'), table_name='department')
    op.drop_table('department')
    # ### end Alembic commands ###