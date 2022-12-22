from sqlalchemy import func, extract, select

from PhongMachTu import db, app
from PhongMachTu.models import Patient, Card, Medicine, Card_Medicine, Admin, Container, Bill, Define


def load_admin():
    return Admin.query.all()


def get_admin_by_id(admin_id):
    return Admin.query.get(admin_id)


def add_patient(username, gender, year, address, sign_date):
    user = Patient(username=username.strip(),
                   gender=gender.strip(),
                   year=year.strip(),
                   address=address.strip(),
                   sign_date=sign_date.strip())

    db.session.add(user)
    db.session.commit()


# def add_card(day):
#     card = list(day=day)
#
#     db.session.add(card)
#     db.session.commit()


def load_patient(patient_id=None):
    patient = Patient.query.all()

    if patient_id:
        patient = [p for p in patient if p[patient_id] == int(patient_id)]
    return patient


def get_patient_by_name(username=None):
    patient = Patient.query

    if username:
        patient = Patient.query.filter(Patient.username.contains(username))

    return patient.all()


def get_user_by_id(patient_id):
    return Patient.query.get(patient_id)


def add_card_doctor(symptom, predict, patient_id):
    card = Card(symptom_medicine=symptom.strip(),
                predict_medicine=predict.strip(),
                patient_id=patient_id)
    db.session.add(card)
    return card


def add_medicine(name, type, amount, instruction):
    medicine = Medicine(name=name,
                        type=type,
                        amount=amount,
                        instruction=instruction)
    db.session.add(medicine)
    db.session.commit()
    return medicine


def save_card_medicine(card_id, medicine_id):
    card_medicine = Card_Medicine(card_id=card_id, medicine_id=medicine_id)
    db.session.add(card_medicine)
    db.session.commit()


def container(name):
    container = Patient.query

    if name:
        container = Container.query.filter(Container.name.contains(name))

    return container.all()


def sign_date(sign_date):
    patient = Patient.query

    if sign_date:
        patient = Patient.query.filter(Patient.sign_date.contains(sign_date))

    return patient.all()


def read_patients(patient_id=None, username=None, page=1):
    patient = Patient.query

    if patient_id:
        patient = [p for p in patient if p[id] == int(patient_id)]
    if username:
        patient = [p for p in patient if p[username] == username]

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size

    return patient.slice(start, end).all()


def save_bills(money_test, money_medicine, total, patient_id):
    bill = Bill(money_test=money_test,
                money_medicine=money_medicine,
                total=total,
                patient_id=patient_id)

    db.session.add(bill)
    db.session.commit()


def stats_revenue(sign_date=None):
    query = db.session.query(Bill.id, Patient.username, Bill.total)\
                      .join(Patient, Bill.patient_id.__eq__(Patient.id))\

    if sign_date:
        query = query.filter(Patient.sign_date.__eq__(sign_date))
    print(sign_date)
    return query.group_by(Patient.sign_date, Bill.id).all()


def register(name, password):
    admin = Admin(name=name,
                  password=password)

    db.session.add(admin)
    db.session.commit()


def money_test(define_id):
    return Define.query.get(define_id)


def get_container_by_name(name):
    return Container.query.filter(name)


def get_card_medicine_by_card_id(card_id):
    return Card_Medicine.query.filter(card_id)


def get_card_by_patient_id(patient_id):
    return Card.query.filter(patient_id)


# def name()
#     query = db.session.query(price
#     from Medicine
#     where amount > 10