from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from PhongMachTu import app, db
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime


# class UserRole(UserEnum):
#     USER = 1
#     ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Admin(BaseModel):
    __tablename__ = 'Admin'

    name = Column(String(50), nullable=False)
    major = Column(String(50), nullable=False)
    patients = relationship('Patient', backref='admin', lazy=False)

    def __str__(self):
        return self.name


class Patient(BaseModel):
    __tablename__ = 'Patient'

    username = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    year = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    joined_date = Column(DateTime, default=datetime.now())
    # user_role = Column(Enum(UserRole), default=UserRole.USER)
    doctor_id = Column(Integer, ForeignKey(Admin.id))

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()