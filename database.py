from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:Charles2001@localhost:3306/Application'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False, bind=engine)
Base = declarative_base()