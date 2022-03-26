from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from kanban.objects import User

# registration form
class register_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

    # username check, if exists
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: raise ValidationError('Username already registered')

    # email check, if exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user: raise ValidationError('Email already registered')

# login form
class login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')