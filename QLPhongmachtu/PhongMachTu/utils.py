from PhongMachTu import db
from PhongMachTu.models import Patient, Card


def add_patient(username, gender, year, address):
    user = Patient(username=username.strip(),
                   gender=gender.strip(),
                   year=year.strip(),
                   address=address.strip())

    db.session.add(user)
    db.session.commit()


def load_patient(patient_id=None, username=None):
    patient = Patient.query.all()

    if patient_id:
        patient = [p for p in patient if p[id] == int(patient_id)]
    if username:
        patient = [p for p in patient if p[username] == username]
    return patient


def get_user_by_id(patient_id):
    return Patient.query.get(patient_id)


def add_card(patient_date, patient_id):
    card = Card(patient_date=patient_date, patient_id=patient_id)

    db.session.add(card)
    db.session.commit()

