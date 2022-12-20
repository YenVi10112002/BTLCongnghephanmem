from urllib.parse import quote
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '@uihksfknkrkj4h2ỉh4r34jj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/hosobn?charset=utf8mb4' % quote('Thanh@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE']=2
db = SQLAlchemy(app=app)
login = LoginManager(app=app)