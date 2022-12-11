from PhongMachTu import db
from PhongMachTu.models import Patient


def add_patient(username, gender, year, address):
    user = Patient(username=username.strip(),
                   gender=gender.strip(),
                   year=year.strip(),
                   address=address.strip())

    db.session.add(user)
    db.session.commit()


