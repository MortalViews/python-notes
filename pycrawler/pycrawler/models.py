from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column, Integer, String)

Session = sessionmaker()
engine = create_engine('sqlite:////tmp/pycrawler.db', echo=True)
Session.configure(bind=engine)
Base = declarative_base()


class Link(Base):
    __tablename__= 'link'
    id=Column(Integer,primary_key=True)
    url=Column(String(400))
    state=Column(String(10),default='pending')
    depth=Column(Integer)
    error_msg=Column(String(400))
    
    
