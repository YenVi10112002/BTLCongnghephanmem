from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from PhongMachTu import app
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


# class BaseModel(db.Model):
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True, autoincrement=True)


#
# class User(BaseModel):
#     name = Column(String(50), nullable=False)
#     username = Column(String(50), nullable=False)
#     password = Column(String(50), nullable=False)
#     avatar = Column(String(100), nullable=False)
#     active = Column(Boolean, default=True)
#     user_role = Column(Enum(UserRole), default=UserRole.USER)
#     receipts = relationship('Receipt', backref='user', lazy=True)
#
#     def __str__(self):
#         return self.name