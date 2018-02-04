from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
metadata = Base.metadata
db_session = scoped_session(sessionmaker())
engine = create_engine("mysql://root:root@localhost:3306/tg_quest_bot", encoding='utf-8')

db_session.configure(bind=engine)
