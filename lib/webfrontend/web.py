from flask import Flask
from lib.utils import *
from .ext import *
from .routes import auth

web = Flask(__name__,static_folder='static',static_url_path='/static/',template_folder='templates')
web.config['SECRET_KEY']=config_read("header","secret_key")
web.config['SQLALCHEMY_DATABASE_URI'] = config_read("db","SQLALCHEMY_DATABASE_URI")
web.jinja_env.auto_reload = True
web.register_blueprint(auth)
login_manager.init_app(web)
db.init_app(web)
web.run('0.0.0.0',5000,True)