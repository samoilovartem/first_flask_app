"""Comment model added

Revision ID: bc1a1b781a93
Revises: 50c8bb0b91fa
Create Date: 2022-07-19 17:53:25.542233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1a1b781a93'
down_revision = '50c8bb0b91fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_news_id'), 'comment', ['news_id'], unique=False)
    op.create_index(op.f('ix_comment_user_id'), 'comment', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_user_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_news_id'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
