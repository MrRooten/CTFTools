from db.model import Module
from sqlalchemy import *
from sqlalchemy.orm import *
'''
engine = create_engine("sqlite:///:memory:")
Module.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

module = Module(m_name='abc',m_path='path',m_type='type',description='descript')
session.add(module)
session.commit()

'''

from db.operationDB import *
