from PhongMachTu import db
from PhongMachTu.models import Patient, list


def add_patient(username, gender, year, address):
    user = Patient(username=username.strip(),
                   gender=gender.strip(),
                   year=year.strip(),
                   address=address.strip())

    db.session.add(user)
    db.session.commit()


def add_card(day):
    card = list(day=day)

    db.session.add(card)
    db.session.commit()

def load_patient():
    return Patient.query.all()

