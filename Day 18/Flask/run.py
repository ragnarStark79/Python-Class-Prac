import os
from datetime import timedelta

from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

# Session configuration
# Prefer an environment variable so cookies remain valid across restarts.
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=timedelta(days=7),
)



gacha = ""

@app.route('/', methods=['GET', 'POST'])
def home():
    # If already logged in, don't show the login form again.
    if request.method == 'GET' and session.get('is_authenticated'):
        return redirect(url_for('dashboard'))
    incoming = ""

    if request.method == 'POST':
        incoming = request.form.get('email3') or ""
        password = request.form.get('password') or ""
        print(f"Received email: {incoming}")

        # check admin credentials, then set session and redirect to dashboard
        if incoming == 'admin@email.com' and password == 'pass':
            session.clear()
            session.permanent = True
            session['is_authenticated'] = True
            session['user_email'] = incoming
            return redirect(url_for('dashboard'))

        # invalid credentials: ensure user is logged out (don't wipe unrelated session values)
        session.pop('is_authenticated', None)
        session.pop('user_email', None)
        return render_template('index.html', data=incoming, password_received=bool(password))

    return render_template('index.html', data=incoming, password_received=False)


@app.route('/dashboard')
def dashboard():
    if not session.get('is_authenticated'):
        return redirect(url_for('home'))

    Author = {
        'name': 'Ragnar',
        'profession': 'Warrior',
    }

    return render_template('dashboard.html', **Author)
  
@app.route('/dashboard/<gacha>')
def gacha(gacha):
  if not session.get('is_authenticated'):
    return redirect(url_for('home'))
  
  return f"<div style='display: flex; justify-content: center; align-items: center; height: 100vh;'><h1 style='text-align: center;'>Welcome to the URL parameter! You selected: {gacha}</h1></div>"

@app.route("/market")
def market():
    if session.get('is_authenticated'):
        return render_template('market.html')
    else:
        return redirect(url_for('home'))
    
    
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))



if __name__ == '__main__':
    # For local dev over HTTP keep Secure=False.
    # When deploying behind HTTPS, consider: app.config['SESSION_COOKIE_SECURE'] = True
    app.run(debug=True, port=5001)