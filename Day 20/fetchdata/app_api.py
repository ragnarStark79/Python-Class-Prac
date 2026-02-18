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

import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"

class Api_form(FlaskForm):

    input = StringField("Email", validators=[DataRequired(), Email()])
    button = SubmitField("Checking the Email")


@app.route("/", methods=["GET","POST"])
def home():
    form = Api_form()
    if form.validate_on_submit():
        email = form.input.data
        print(email)
        #abc@ab.com
        response = requests.get(f"https://api.xposedornot.com/v1/check-email/{email}").json()
        print(response)
        return render_template("api.html", form=form, response=response)
    
    print("get request")
    return render_template("api.html", form=form)


app.run(debug=True, port=4000)