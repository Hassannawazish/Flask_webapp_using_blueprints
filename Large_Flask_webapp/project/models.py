from project.init import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from database.setup import Base
from sqlalchemy import Column, Integer, String, Text, text, Float, Boolean, ForeignKey

from sqlalchemy import Column, Integer, Text, text, Float, Boolean, ForeignKey
from sqlalchemy.orm import backref, relationship
from database.setup import Base

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash, password)


class userName(Base):
    __tablename__ = 'username'
    id = Column(Integer, primary_key=True)
    user_name = Column(Text)
    sugg = relationship("Suggestion", back_populates="username")
    def __init__(self, name):
        self.user_name = name


class Suggestion(Base):
    __tablename__ = 'suggestion'
    id = Column(Integer, primary_key=True)
    sugg = Column(Text)
    id_foreign = Column(Integer, ForeignKey('username.id'))
    username = relationship(argument='userName', back_populates="sugg")
    def __init__(self, sugg, id):
        self.sugg = sugg
        self.id_foreign = id