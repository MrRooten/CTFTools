from datetime import datetime
from .ext import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user = db.Column(db.String(64))
    passowrd = db.Column(db.String(256))
    email = db.Column(db.String(40))

    def __repr__(self):
        return "<User(user='%s',email='%s')>" % (self.user,self.email)

    def set_password(self,password):
        self.passowrd = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.passowrd,password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

