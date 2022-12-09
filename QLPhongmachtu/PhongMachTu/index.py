from flask import render_template, request, url_for
from PhongMachTu import app
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=['get', 'post'])
def user_login():
    return render_template('functions/login.html')


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
