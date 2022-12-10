from flask import render_template, request, url_for
from PhongMachTu import app, utils
from flask_login import login_user, logout_user, current_user, login_required


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


# def admin_login():
#     username = request.form['username']
#     password = request.form['password']
#
#     user = dao.auth_user(username=username, password=password)
#     if user:
#         login_user(user=user)
#
#     return redirect('/admin')


if __name__ == '__main__':
    app.run(debug=True)
