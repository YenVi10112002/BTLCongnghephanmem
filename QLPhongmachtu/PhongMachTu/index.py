import hashlib
import pdb
from flask_admin import Admin
from flask import render_template, request, url_for, redirect, session, jsonify
from PhongMachTu import app, utils, login
from flask_login import login_user, logout_user, current_user, login_required
from PhongMachTu.models import Admin


@login.user_loader
def admin_load(admin_id):
    return utils.get_admin_by_id(admin_id=admin_id)


@app.route('/', methods=['get', 'post'])
def home():
    success_msg = ''
    if request.method.__eq__('POST'):
        username = request.form['username']
        gender = request.form['gender']
        year = request.form['year']
        address = request.form['address']
        sign_date = request.form['sign_date']
        try:
            utils.add_patient(username=username,
                              gender=gender,
                              year=year,
                              address=address,
                              sign_date=sign_date)
            success_msg = 'Thanh cong'
        except:
            success_msg = 'Khong thanh cong'

    return render_template('index.html', success_msg=success_msg)


@app.route("/create/<int:admin_id>")
def create(admin_id):
    patient_id = request.args.get("id")
    patient = utils.load_patient(patient_id=patient_id)
    return render_template("functions/doctor.html", patient=patient, admin_id=admin_id)


@app.route("/patients/<int:admin_id>")
def patient(admin_id):
    username = request.args.get("username")
    patients = utils.get_patient_by_name(username=username)
    return render_template("functions/info.html", patient=patients, admin_id=admin_id)


# tìm thuốc
@app.route("/search/<int:admin_id>")
def search(admin_id):
    name = request.args.get("name")
    container = utils.container(name=name)
    return render_template("functions/info_medicine.html", container=container, admin_id=admin_id)


@app.route("/loc")
def loc():
    sign_date = request.args.get("sign_date")
    sign_date = utils.sign_date(sign_date=sign_date)
    return render_template("functions/list1.html", sign_date=sign_date)


@app.route("/card/<int:patient_id>/<int:admin_id>", methods=['get', 'post'])
def card(patient_id, admin_id):
    patient = utils.get_user_by_id(patient_id=patient_id)
    return render_template("functions/examination_card.html", patient=patient, admin_id=admin_id)


@app.route("/add_card_doctor/<int:patient_id>/<int:admin_id>", methods=['get', 'post'])
def add_card_doctor(patient_id, admin_id):
    msg = ''
    if request.method.__eq__('POST'):
        symptom = request.form["symptom"]
        predict = request.form["predict"]
        name_medicine = request.form['name_medicine']
        type = request.form['type']
        amount = request.form['amount']
        instruction = request.form['instruction']

        try:
            card = utils.add_card_doctor(symptom=symptom,
                                         predict=predict,
                                         patient_id=patient_id)
            medicine = utils.add_medicine(name=name_medicine, type=type, amount=amount, instruction=instruction)
            patient = utils.get_user_by_id(patient_id=patient_id)
            admin = utils.get_admin_by_id(admin_id=admin_id)
            patient.admin_id = admin.id
            db.session.add(patient)
            db.session.commit()
            utils.save_card_medicine(card_id=card.id, medicine_id=medicine.id)
            msg = 'Thanh cong'
        except:
            msg = 'Khong thanh cong'
    return render_template('functions/doctor.html', msg=msg, admin_id=admin_id)


@app.route("/login", methods=['get', 'post'])
def login():
    # name = request.form['username']
    # password = request.form['password']
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        password = request.form.get('password')
        admins = utils.load_admin()
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        for ad in admins:
            if ad.name == name and ad.password == password:
                if ad.name == "doctor":
                    return render_template('functions/doctor.html', admin_id=ad.id)
                if ad.name == "nurse":
                    return render_template('functions/nurse.html', admin_id=ad.id)
            else:
                err_msg = 'User hoac mat khau khong chinh xac'

    return render_template('functions/login.html', err_msg=err_msg)


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


@app.route('/list')
def list():
    patient = utils.load_patient()
    return render_template('functions/nurse.html', patient=patient)


@app.route('/edit', methods=['get', 'post'])
def edit():
    patient = utils.load_patient()
    return render_template('functions/list.html', patient=patient)


@app.route("/bill/<int:patient_id>")
def bill(patient_id):
    define_id = 1
    define = utils.money_test(define_id=define_id)
    # c = utils.get_card_by_patient_id(patient_id)
    # card_id = c.card_id
    # m = utils.get_card_medicine_by_card_id(card_id)
    # # số lượng mỗi loại thuốc
    # a = m.medicine_id.amount
    # # tên thuốc
    # t = m.medicine_id.name
    # money = utils.get_container_by_name(t)
    # money_medicine = a * money

    pa = utils.get_user_by_id(patient_id=patient_id)
    return render_template("functions/reciepts.html", patient=pa, define=define)


@app.route("/bill/<int:patient_id>", methods=['get', 'post'])
def save_bill(patient_id):
    msg=''
    if request.method.__eq__('POST'):
        define_id = 1
        define = utils.money_test(define_id=define_id)
        money_test = define.money
        money_medicine = request.form["money_medicine"]
        total = request.form["total"]

        try:
            utils.save_bills(money_test=money_test,
                             money_medicine=money_medicine,
                             total=total,
                             patient_id=patient_id)
            msg = "Thành công"
        except Exception as ex:
            msg = "Lỗi" + str(ex)
    return render_template("functions/nurse.html", msg=msg)


@app.route('/page')
def page():
    pa = request.args.get('page', 1)
    patient = utils.read_patients(page=int(pa))
    return render_template('functions/nurse.html', patient=patient, pa=pa)


@app.route('/pay')
def pay():
    patient = utils.load_patient()
    return render_template('functions/pay.html', patient=patient)


# nurse
# @app.route("/add_patient_date", methods=['get', 'post'])
# def add_patient_date():
#     msg = ''
#     if request.method.__eq__('POST'):
#         day = request.form.get("patient_date")
#
#         try:
#             utils.add_card(day=day)
#             msg = 'Thanh cong'
#         except:
#             msg = 'Khong thanh cong'
#     return render_template('functions/nurse.html', msg=msg)


if __name__ == '__main__':
    from PhongMachTu.admin import *

    app.run(debug=True)
