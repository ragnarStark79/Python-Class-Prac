from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecret"

# Simulated database
balance = 1000

@app.route("/")
def login():
    session["user"] = "Prashant"
    return redirect(url_for("dashboard"))

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global balance

    if "user" not in session:
        return "Not logged in", 403

    if request.method == "POST":
        amount = request.form.get("amount", type=int)

        if amount and amount > 0:
            balance -= amount
            print("Money transferred:", amount)
            print("New balance:", balance)

    return render_template("amount.html", balance=balance)

if __name__ == "__main__":
    app.run(debug=True)
