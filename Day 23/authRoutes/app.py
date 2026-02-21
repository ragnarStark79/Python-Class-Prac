from flask import Flask
from models import db, User
from flask_login import LoginManager

app = Flask(__name__)

# secret key for login session
app.config['SECRET_KEY'] = "secret123"

# ORM database config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

db.init_app(app)


# LOGIN MANAGER

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# import routes
from routes import *

# create DB
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
