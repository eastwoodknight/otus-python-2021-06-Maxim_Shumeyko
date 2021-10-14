"""Initial migration

Revision ID: 5532e5b6fd8d
Revises: 
Create Date: 2021-09-12 13:04:39.532347

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from models.blogpost import Blogpost
from models.author import Author


# revision identifiers, used by Alembic.
revision = '5532e5b6fd8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('subtitle', sa.String(length=50), nullable=True),
    sa.Column('date_posted', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author_id')
    )
    # ### end Alembic commands ###

    # add initial data set
    session = Session(bind=op.get_bind())

    bjorn = Author(name='Bjorn')
    guido = Author(name='Guido')
    brendan = Author(name='Brendan')

    session.add_all([guido, bjorn, brendan])
    session.commit()
    
    post1 = Blogpost(
        title='The incredible adventures of the snake charmer',
        subtitle='Spam Eggs',
        author=guido,
    )

    post2 = Blogpost(
        title='I see no pluses in pure C',
        subtitle='',
        author=bjorn,
    )

    post3 = Blogpost(
        title='No one writes scripts to the colonel Java',
        subtitle='new subtitle',
        author=brendan,
    )

    session.add_all([post1, post2, post3])
    session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogposts')
    op.drop_table('authors')
    # ### end Alembic commands ###

