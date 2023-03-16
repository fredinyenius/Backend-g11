"""cambien datos tabal usuario

Revision ID: 1557fc71cc34
Revises: 37d9e0350f2c
Create Date: 2023-03-10 20:06:29.236204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1557fc71cc34'
down_revision = '37d9e0350f2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('correo',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('nombre',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('apellido',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('apellido',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('nombre',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('correo',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
