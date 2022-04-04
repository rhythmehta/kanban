from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = '**********'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#authentication
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from kanban import routes
