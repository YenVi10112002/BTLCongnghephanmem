import hashlib

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from PhongMachTu import app, db
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime, date


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
    is_active = Column(Boolean, default=1)
    patients = relationship('Patient', backref='admin', lazy=False)

    def __str__(self):
        return self.name


class Patient(BaseModel, UserMixin):
    __tablename__ = 'Patient'

    username = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    year = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    sign_date = Column(String(100), nullable=False)
    admin_id = Column(Integer, ForeignKey(Admin.id), nullable=True)
    cards = relationship('Card', backref='patient', lazy=False)
    bill_id = relationship('Bill', backref='patient', lazy=True)

    def __str__(self):
        return self.name


class Container(BaseModel):
    __tablename__ = 'Container'

    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    amount = Column(String(50), nullable=False)
    instruction = Column(String(50), nullable=False)
    cards = relationship('Card', backref='container', lazy=False)
    def __str__(self):
        return self.name


class Card(BaseModel):
    __tablename__ = 'Card'

    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)
    symptom_medicine = Column(String(50), nullable=False)
    predict_medicine = Column(String(50), nullable=False)
    card_medicine = relationship('Card_Medicine', backref='card', lazy=True)
    container_id = Column(Integer, ForeignKey(Container.id), nullable=True)
    def __str__(self):
        return self.name


class Medicine(BaseModel):
    __tablename__: 'Medicine'

    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    amount = Column(String(50), nullable=False)
    instruction = Column(String(50), nullable=False)
    card_medicine = relationship('Card_Medicine', backref='medicine', lazy=True)

    def __str__(self):
        return self.name


class Card_Medicine(BaseModel):
    card_id = Column(Integer, ForeignKey(Card.id), nullable=True)
    medicine_id = Column(Integer, ForeignKey(Medicine.id), nullable=True)


class Bill(BaseModel):
    __tablename__ = 'Bill'

    money_test = Column(Integer)
    money_medicine = Column(Integer)
    total = Column(Integer)
    patient_id = Column(Integer, ForeignKey(Patient.id), nullable=False)

    def __str__(self):
        return self.name


class Define(BaseModel):
    __tablename__ = 'Define'

    amount_bn = Column(Integer)
    money = Column(Integer)


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

        patient = Patient(username='Thanh', gender='Female', year=2002, address="HJHJHẤDNSV DSVJDSV",
                          sign_date="19/12/2022")
        patient1 = Patient(username='Vi', gender='Female', year=2002, address="HJHJHẤDNSV DSVJDSV",
                           sign_date="19/12/2022")
        db.session.add(patient)
        db.session.add(patient1)

        container = Container(name="Atropin sulfat", type="ống", amount=500, instruction="Tiêm vào người")
        container1 = Container(name="Acetylsalicylic acid", type="viên", amount=500, instruction="dùng để uống")
        container2 = Container(name="Meloxicam", type="viên", amount=500, instruction="dùng để uống")
        container3 = Container(name="Paracetamol (acetaminophen)", type="vỉ", amount=500, instruction="dùng để uống")
        container4 = Container(name="Spironolacton", type="viên", amount=500, instruction="dùng để uống")

        # medicine = Medicine(name="Atropin sulfat")
        # medicine1 = Medicine(name="Acetylsalicylic acid")
        # medicine2 = Medicine(name="Meloxicam")
        # medicine3 = Medicine(name="Paracetamol (acetaminophen)")
        # medicine4 = Medicine(name="Spironolacton")
        db.session.add(container)
        db.session.add(container1)
        db.session.add(container2)
        db.session.add(container3)
        db.session.add(container4)
        db.session.commit()
