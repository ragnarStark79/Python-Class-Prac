from flask import Flask, render_template, request
from forms import Api_form
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


def fetch_breach_data(email):
    try:
        url = f"https://api.xposedornot.com/v1/check-email/{email}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.json(), None
        elif res.status_code == 404:
            return None, "clean"   # no breach found
        else:
            return None, f"API returned status {res.status_code}"
    except requests.exceptions.Timeout:
        return None, "Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return None, "Could not connect to the breach API."
    except Exception as e:
        return None, str(e)


@app.route("/", methods=["GET", "POST"])
def home():
    form = Api_form()
    response = None
    error = None
    email_checked = None

    if form.validate_on_submit():
        email_checked = form.email.data
        response, error = fetch_breach_data(email_checked)

    return render_template(
        "api.html",
        form=form,
        response=response,
        error=error,
        email_checked=email_checked,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
