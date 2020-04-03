from sqlalchemy import *
from lib.utils import config_write
import configparser

config = configparser.RawConfigParser()
config.read("./config.ini")

is_createDB = config["db"]["is_createDB"]

def create_db():
    from db.model import Module
    engine = create_engine("sqlite:///db/module.db")
    Module.metadata.create_all(engine)
    config_write("db","is_createDB",1)
if is_createDB ==  0:
    create_db()