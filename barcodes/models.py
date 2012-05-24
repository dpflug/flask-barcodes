from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    email = Column(String(200), unique=True)
    created = Column(DateTime)
    used_barcode = Column(Boolean())

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        # Shouldn't need access to below fields
        self.created = datetime.now()
        self.used_barcode = False

    def __repr__(self):
        return '<User {0.name}>'.format(self)
