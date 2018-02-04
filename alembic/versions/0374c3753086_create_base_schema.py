"""create base schema

Revision ID: 0374c3753086
Revises: 
Create Date: 2018-01-13 23:53:31.915161

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '0374c3753086'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tlg_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(100)),
        sa.Column('second_name', sa.String(100)),
        sa.Column('lang_code', sa.String(100)),
        sa.Column('user_name', sa.String(100)),
        sa.Column('is_bot', sa.Boolean),
        sa.Column('creation_date', sa.DateTime, default=datetime.datetime.utcnow),
        sa.Column('join_date', sa.DateTime),
    )

    op.create_table(
        'tlg_chats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.Text),
        sa.Column('chat_type', sa.String(100)),
        sa.Column('description', sa.Text),
        sa.Column('first_name', sa.String(100)),
        sa.Column('second_name', sa.String(100)),
        sa.Column('user_name', sa.String(100)),
        sa.Column('invite_link', sa.Text),
        sa.Column('is_all_members_admins', sa.Boolean),
        sa.Column('creation_date', sa.DateTime,  default=datetime.datetime.utcnow)
    )

    op.create_table(
        'tlg_messages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('from_user_id', sa.Integer, sa.ForeignKey("tlg_users.id")),
        sa.Column('date', sa.DateTime,  default=datetime.datetime.utcnow),
        sa.Column('chat_id', sa.Integer, sa.ForeignKey("tlg_chats.id")),
        sa.Column('forward_from_id', sa.Integer, sa.ForeignKey("tlg_users.id")),
        sa.Column('forward_from_chat_id', sa.Integer, sa.ForeignKey("tlg_chats.id")),
        sa.Column('forward_date', sa.DateTime),
        sa.Column('reply_to_message_id', sa.Integer, sa.ForeignKey("tlg_messages.id")),
        sa.Column('parent_message_id', sa.Integer, sa.ForeignKey("tlg_messages.id")),
        sa.Column('text', sa.Text),
        sa.Column('entity_info', sa.Text),
    )

    op.create_table(
        'tlg_chat_members',
        sa.Column('user_id', sa.Integer, sa.ForeignKey("tlg_users.id"), primary_key=True, ),
        sa.Column('chat_id', sa.Integer,  sa.ForeignKey("tlg_chats.id"), primary_key=True),
        sa.Column('status', sa.String(100)),
        sa.Column('creation_date', sa.DateTime, default=datetime.datetime.utcnow),
        sa.Column('until_date', sa.DateTime)
    )


    op.create_table(
        'questions_progress',
        sa.Column('chat_id', sa.Integer, sa.ForeignKey("tlg_chats.id"), primary_key=True),
        sa.Column('question_number', sa.Integer),
        sa.Column('passed', sa.Boolean),
        sa.Column('tries', sa.Integer),
        sa.Column('creation_date', sa.DateTime, default=datetime.datetime.utcnow),
    )

    conn = op.get_bind()
    tables = conn.execute("SHOW TABLES")
    for t in tables:
        conn.execute(sa.sql.text('ALTER table %s CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci' % t[0]))


def downgrade():
    pass
