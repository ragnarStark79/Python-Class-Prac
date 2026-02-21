from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, EqualTo, DataRequired
from wtforms import ValidationError
from .models import db, User

class LoginForm(FlaskForm):
    email  = StringField("Email", validators=[DataRequired(),Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already register")
        
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already Exist")