from flask import Flask

#importação do SQL Alchemy
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '3247f73eee75b941aa3889f747042b69'

#Configuração do SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.app_context().push()
database = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from comunidade import routes