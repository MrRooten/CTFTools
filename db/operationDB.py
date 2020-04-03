from sqlalchemy import *
from sqlalchemy.orm import *
from db.model import Module
engine = create_engine("sqlite:///db/module.db")
Module.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def insertModule(m_name,m_type,m_path,description):
    session.add(Module(m_name=m_name,m_path=m_path,m_type=m_type,description=description))
    session.commit()

def deleteModule():
    pass
