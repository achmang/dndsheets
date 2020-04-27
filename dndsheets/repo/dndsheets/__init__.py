from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisIsASecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ACHEST/Desktop/Dev/Web/dndsheets/repo2/dndsheets/database.db'
Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)

from dndsheets import routes
