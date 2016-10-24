"""empty message

Revision ID: dbb79ff12e45
Revises: c3676a5f81de
Create Date: 2016-05-23 15:36:42.015391

"""

# revision identifiers, used by Alembic.
revision = 'dbb79ff12e45'
down_revision = 'c3676a5f81de'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social_link',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('link', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['event_id'], [u'events.id'], name=u'social_link_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'social_link_pkey')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('social_link')
    ### end Alembic commands ###