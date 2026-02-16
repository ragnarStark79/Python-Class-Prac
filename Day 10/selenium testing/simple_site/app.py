from __future__ import annotations

import os

from flask import Flask, redirect, render_template, request, session, url_for


def create_app() -> Flask:
    app = Flask(__name__)
    # For a class/demo project this is fine; for real apps use a proper secret in env.
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/login")
    def login_get():
        return render_template("login.html", error=None)

    @app.post("/login")
    def login_post():
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == "student" and password == "password123":
            session["user"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid username or password")

    @app.get("/dashboard")
    def dashboard():
        user = session.get("user")
        if not user:
            return redirect(url_for("login_get"))
        return render_template("dashboard.html", user=user)

    @app.post("/logout")
    def logout():
        session.clear()
        return redirect(url_for("home"))

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5001")), debug=True)
