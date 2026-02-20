from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, TextAreaField,
    IntegerField, BooleanField, RadioField,
    SelectField, SelectMultipleField,
    FileField, SubmitField, HiddenField
)
from wtforms.validators import (
    DataRequired, Length, Email,
    EqualTo, NumberRange
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
class RegisterForm(FlaskForm):
    username = StringField("Username",
        validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email",
        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
        validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password",
        validators=[DataRequired(), EqualTo("password")])
    age = IntegerField("Age",
        validators=[NumberRange(min=18, max=100)])

    bio = TextAreaField("Bio")

    gender = RadioField("Gender",
        choices=[("male","Male"), ("female","Female")])

    role = SelectField("Role",
        choices=[("user","User"), ("admin","Admin")])

    skills = SelectMultipleField("Skills",
        choices=[("python","Python"), ("pac","Flask"), ("security","Security")])

    remember = BooleanField("Remember Me")

    profile_pic = FileField("Upload Profile Picture")

    user_id = HiddenField(default="12345")

    submit = SubmitField("Register")

class Login(FlaskForm):
    email = StringField("Login Email", validators=[DataRequired(), Email()])
    password = PasswordField("Login Password", validators=[DataRequired()])
    submit = SubmitField("Login")

@app.route("/login", methods=["GET","POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        return redirect(url_for("login"))
    return render_template("login.html", form=form)

#########################################

@app.route("/", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        # if method == "POST" and validation
        flash(f"Welcome {form.username.data}")
        return redirect(url_for("register"))

    return render_template("index.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)



