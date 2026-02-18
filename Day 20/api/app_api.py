from flask import Flask, render_template, request, session, redirect, url_for
from forms import Api_form
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


@app.route("/", methods=["GET", "POST"])
def home():
  form = Api_form()
  if form.validate_on_submit():
    email = form.email.data
    print(email)
    
    response = requests.get(f"https://api.xposedornot.com/v1/check-email?email={email}").json()
    print(response)
    return render_template("api.html", form=form, response=response)
  
  print("get request")
  return render_template("api.html", form=form)

