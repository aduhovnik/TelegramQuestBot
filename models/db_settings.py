import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA

Base = declarative_base()
metadata = Base.metadata
db_session = scoped_session(sessionmaker())

DB_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
logging.warning(f'DB_URI: {DB_URI}, DB_SCHEMA: {DB_SCHEMA}')

engine = create_engine(DB_URI,
                       connect_args={'options': f'-csearch_path={DB_SCHEMA}'})

db_session.configure(bind=engine)
