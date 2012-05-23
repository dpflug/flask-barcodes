from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    email = Column(String(200), unique=True)
    created = Column(DateTime)

    def __init__(self, name=None, email=None, created=datetime.now()):
        self.name = name
        self.email = email
        self.created = datetime.now()

    def __repr__(self):
        return '<User {0.name}>'.format(self)
