import hashlib
from flask import render_template, request, url_for
from PhongMachTu import app, utils
from flask_login import login_user, logout_user, current_user, login_required

from PhongMachTu.models import Admin


@app.route('/', methods=['get', 'post'])
def home():
    success_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        gender = request.form.get('gender')
        year = request.form.get('year')
        address = request.form.get('address')

        try:
            utils.add_patient(username=username,
                              gender=gender,
                              year=year,
                              address=address)
            success_msg = 'Thanh cong'
        except:
            success_msg = 'Khong thanh cong'

    return render_template('index.html', success_msg=success_msg)


# @app.route("/login", methods=['get', 'post'])
# def user_login():
#     return render_template('functions/login.html')


@app.route("/login", methods=['get', 'post'])
def login():
    # name = request.form['username']
    # password = request.form['password']
    err_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        password = request.form.get('password')
        admins = Admin.query.all()
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        for ad in admins:
            if ad.name == name and ad.password == password:
                if ad.name == "doctor":
                    return render_template('functions/doctor.html')
                if ad.name == "nurse":
                    return render_template('functions/nurse.html')
                if ad.name == "manager":
                    return render_template('functions/manager.html')
            else:
                err_msg = 'User hoac mat khau khong chinh xac'

    return render_template('functions/login.html', err_msg=err_msg)


if __name__ == '__main__':
    app.run(debug=True)
