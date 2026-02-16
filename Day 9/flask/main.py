from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/flask")
def flask():
  return"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Intro Page</title>
    </head>
    <body>
        <h1>Welcome to the Flask Page</h1>
        <p>This is a simple Flask application.</p>
    </body>
    </html>
"""

if __name__ == "__main__":
    app.run(debug=True)
