from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "supersecretkey"

balance = 100000

class TransferForm(FlaskForm):
    to = StringField("Receiver", validators=[DataRequired()])
    amount = IntegerField("Amount", validators=[DataRequired()])
    submit = SubmitField("Transfer")


@app.route("/", methods=["GET", "POST"])
def home():
    global balance
    form = TransferForm()

    if form.validate_on_submit():
        balance -= form.amount.data

        print("Legitimate Transfer")
        print(f"Sent ₹{form.amount.data} to {form.to.data}")
        print(f"Remaining Balance: ₹{balance}")

    return render_template("secure_bank.html", form=form, balance=balance)


if __name__ == "__main__":
    app.run(debug=True)
