from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Module(Base):
    __tablename__ = 'modules'

    mid = Column(Integer,primary_key=True,autoincrement=True)
    m_name = Column(String(20))
    m_path = Column(String(50),index=True)
    description = Column(Text)
    m_type = Column(String(30))

    def __repr__(self):
        return "<Module(m_name='%s',m_path='%s',type='%s')>" % (self.m_name,self.m_path,self.m_type)

