from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel as Base

metadata = Base.metadata


class TlgChatMember(Base):
    __tablename__ = 'tlg_chat_members'

    user_id = Column(ForeignKey('tlg_users.id'), primary_key=True, nullable=False)
    chat_id = Column(ForeignKey('tlg_chats.id'), primary_key=True, nullable=False, index=True)
    status = Column(String(100))
    creation_date = Column(DateTime)
    until_date = Column(DateTime)

    chat = relationship('TlgChat')
    user = relationship('TlgUser')


class TlgChat(Base):
    __tablename__ = 'tlg_chats'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    chat_type = Column(String(100))
    description = Column(String)
    first_name = Column(String(100))
    second_name = Column(String(100))
    user_name = Column(String(100))
    invite_link = Column(String)
    is_all_members_admins = Column(Integer)
    creation_date = Column(DateTime)


class QuestionsProgres(Base):
    __tablename__ = 'questions_progress'

    id = Column(Integer, primary_key=True)
    chat_id = Column(ForeignKey('tlg_chats.id'))
    question_number = Column(Integer)
    passed = Column(Integer)
    tries = Column(Integer)
    creation_date = Column(DateTime)


class TlgMessage(Base):
    __tablename__ = 'tlg_messages'

    id = Column(Integer, primary_key=True)
    from_user_id = Column(ForeignKey('tlg_users.id'), index=True)
    date = Column(DateTime)
    chat_id = Column(ForeignKey('tlg_chats.id'), index=True)
    forward_from_id = Column(ForeignKey('tlg_users.id'), index=True)
    forward_from_chat_id = Column(ForeignKey('tlg_chats.id'), index=True)
    forward_date = Column(DateTime)
    reply_to_message_id = Column(ForeignKey('tlg_messages.id'), index=True)
    parent_message_id = Column(ForeignKey('tlg_messages.id'), index=True)
    text = Column(String)
    entity_info = Column(String)

    chat = relationship('TlgChat', primaryjoin='TlgMessage.chat_id == TlgChat.id')
    forward_from_chat = relationship('TlgChat', primaryjoin='TlgMessage.forward_from_chat_id == TlgChat.id')
    forward_from = relationship('TlgUser', primaryjoin='TlgMessage.forward_from_id == TlgUser.id')
    from_user = relationship('TlgUser', primaryjoin='TlgMessage.from_user_id == TlgUser.id')
    parent_message = relationship('TlgMessage', remote_side=[id],
                                  primaryjoin='TlgMessage.parent_message_id == TlgMessage.id')
    reply_to_message = relationship('TlgMessage', remote_side=[id],
                                    primaryjoin='TlgMessage.reply_to_message_id == TlgMessage.id')


class TlgUser(Base):
    __tablename__ = 'tlg_users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    second_name = Column(String(100))
    lang_code = Column(String(100))
    user_name = Column(String(100))
    is_bot = Column(Integer)
    creation_date = Column(DateTime)
    join_date = Column(DateTime)
