from flask import Flask,redirect,url_for,render_template,request, jsonify, session
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
import re

app=Flask(__name__)
app.secret_key = "asfnaq3478yr83y4bd8n3487c4"

# demo user data
USERS = {
  "ragnar": generate_password_hash("Password123")
}

def validate_login_input(username: str, password: str):
  errors = []
  username = (username or "").strip()
  password = password or ""
  
  if not username:
    errors.append("Username is required")
  elif not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
    errors.append("Username must be 3-20 chars: letter, number, underscore..")
    
  if not password:
    errors.append("Password is required..")
  elif len(password) <= 8:
    errors.append("Password must be at least 8 characters long..")
    
  return errors

def login_required(view_fn):
  def wrapper(*args, **kwargs):
    if 'username' not in session:
      return redirect(url_for('form'))
    return view_fn(*args, **kwargs)
  wrapper.__name__ = view_fn.__name__
  return wrapper

# {} is used to return a json response
@app.route("/")
def home():
  return render_template('index.html'), 201
  # return {
  #   'name': 'Ragnar'
  # }, 201
  
# escape is used to prevent XSS attack by escaping the special characters in the string
@app.route("/args")
def args():
  name=request.args.get('name', 'Ragnar')
  if name != 'Ragnar':
    return "Unauthorized", 403
  return f"Hello {escape(name)}", 201


@app.route("/about")
def about():
  return render_template('about.html'), 201


# jsonify is used to return a json response with the correct content type and status code
@app.route("/json_data")
def json_data():
  return jsonify(
    {
      'name': 'Ragnar'
    }
  )
  
@app.route("/custom")
def custom():
  name = request.args.get('name', 'Ragnar')
  # &lt; is used to escape the < character and &gt; is used to escape the > character to prevent XSS attack
  name = name.replace('<', '&lt;').replace('>', '&gt;')
  return f"Hello {name}", 201 

@app.route("/form", methods=['GET', 'POST'])
def form():
  if request.method == 'POST':
    name = request.form.get('name', 'Ragnar')
    profession = request.form.get('profession', 'Unknown')
    name = name.replace('<', '&lt;').replace('>', '&gt;')
    profession = profession.replace('<', '&lt;').replace('>', '&gt;')
    return f"Hello {name}, the {profession}", 201
  return render_template('form.html'), 201


if __name__ == '__main__':
  app.run(port=5001,debug=True)