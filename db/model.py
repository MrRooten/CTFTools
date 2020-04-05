from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
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


class User(Base,UserMixin):
    __tablename__ = 'users'

    uid = Column(Integer,primary_key=True,autoincrement=True)
    user = Column(String(20))
    passowrd = Column(String(256))
    email = Column(String(40))

    def __repr__(self):
        return "<User(user='%s',email='%s')>" % (self.user,self.email)

    def set_password(self,password):
        self.passowrd = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.passowrd,password)


