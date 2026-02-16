from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), unique=True, nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  

# def authentication_required(func):
#   def wrapper(*args, **kwargs):
#     authenticated = True
#     if not authenticated:
#       return redirect(url_for('login'))
#     return func(*args, **kwargs)
#   return wrapper

@app.route('/')
def home():
  
  return render_template('index.html')


@app.route("/dashboard")
def dashboard():
  Author = {
      'name' : 'Ragnar',
      'profession' : 'Warrior',
    }
  return render_template('dashboard.html', **Author)


@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/market", methods=['GET', 'POST'])
def market():
  market_items = [
    {'id': 1, 'name': 'Sword', 'price': 100},
    {'id': 2, 'name': 'Shield', 'price': 150},
    {'id': 3, 'name': 'Health Potion', 'price': 50},
  ]
  message = None

  if request.method == 'POST':
    item_id = request.form.get('item_id', type=int)
    selected = next((i for i in market_items if i['id'] == item_id), None)

    if selected is None:
      message = "Invalid item selected."
    else:
      message = f"You bought: {selected['name']} for ${selected['price']}"

  return render_template('market.html', market_items=market_items, message=message)

# Helper to initialize the DB/tables
def init_db():
  with app.app_context():
    db.create_all()

if __name__ == "__main__": 
  init_db()
  app.run(port=5001,debug=True)