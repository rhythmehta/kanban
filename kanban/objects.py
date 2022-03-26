from kanban import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# User db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(16),unique=True,nullable=False)
    email = db.Column(db.String(96),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    todos = db.relationship('Todo',backref="user",lazy=True)

# Todo db to store task info
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    desc = db.Column(db.Text,nullable=False)
    inprogress = db.Column(db.Boolean,default=False)
    completed = db.Column(db.Boolean,default=False)
    due = db.Column(db.DateTime,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))