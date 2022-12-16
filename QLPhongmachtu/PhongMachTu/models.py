import hashlib

import self as self
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
    password = Column(String(100))
    # patients = relationship('Patient', backref='admin', lazy=False)

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
    admin_id = Column(Integer, ForeignKey(Admin.id))

    def __str__(self):
        return self.name


class Card(BaseModel):
    __tablename__ = 'Card'

    patient_date = Column(String(50))
    patient_id = Column(Integer, ForeignKey(Patient.id))

    def __str__(self):
        return self.name


# class list(Patient):
#     __tablename__ = 'list'
#
#     day = Column(DateTime)
#
#     def __str__(self):
#         return self.name

class list(BaseModel):
    __tablename__ = 'list'

    day = Column(DateTime)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        password1 = str(hashlib.md5('1'.encode('utf-8')).hexdigest())
        password2 = str(hashlib.md5('2'.encode('utf-8')).hexdigest())
        password3 = str(hashlib.md5('3'.encode('utf-8')).hexdigest())
        admin1 = Admin(name='doctor', major='Doctor', password=password1)
        admin2 = Admin(name='nurse', major='nurse', password=password2)
        admin3 = Admin(name='manager', major='manager', password=password3)
        db.session.add(admin1)
        db.session.add(admin2)
        db.session.add(admin3)

        patient = Patient(username='Thanh', gender='Female', year=2002, address="HJHJHẤDNSV DSVJDSV")
        patient1 = Patient(username='Vi', gender='Female', year=2002, address="HJHJHẤDNSV DSVJDSV")
        db.session.add(patient)
        db.session.add(patient1)
        db.session.commit()
