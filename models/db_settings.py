from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import MYSQL_CONN_STR

Base = declarative_base()
metadata = Base.metadata
db_session = scoped_session(sessionmaker())
engine = create_engine(MYSQL_CONN_STR, encoding='utf-8')

db_session.configure(bind=engine)
