from flask import render_template
from PhongMachTu import app


@app.route('/')
def home():
    return render_template('functions/nurse.html')


if __name__ == '__main__':
    app.run(debug=True)
