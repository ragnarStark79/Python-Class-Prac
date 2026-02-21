from flask import render_template, redirect, request, url_for, flash
from app import app
from models import db, User, Post
from forms import RegistrationForm, LoginForm, PostForm

from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


# HOME PAGE

@app.route("/")
def home():
    form_login = LoginForm()
    form_register = RegistrationForm()

    if current_user.is_authenticated:
        posts = Post.query.order_by(Post.date.desc()).all()
        return render_template("index.html", posts=posts)
    else:
        return render_template("index.html", posts=None, form_login=form_login, form_register=form_register)


# REGISTER

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = form.role.data

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return redirect("/register")

        user = User(username=username, email=email, password=password, role=role)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect("/login")

    return render_template("register.html", form=form)


# LOGIN

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            # ROLE REDIRECT
            if user.role == "admin":
                return redirect("/admin_dashboard")
            elif user.role == "author":
                return redirect("/author_dashboard")
            else:
                return redirect("/user_dashboard")
        else:
            flash("Login failed. Check email and password.", "danger")
            return redirect("/login")

    return render_template("login.html", form=form)


# LOGOUT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


# DASHBOARDS

@app.route("/admin_dashboard")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "Access denied", 403

    users = User.query.all()
    posts = Post.query.all()
    # Assuming admin.html is the admin dashboard template
    return render_template("admin.html", users=users, posts=posts)


@app.route("/author_dashboard")
@login_required
def author_dashboard():
    if current_user.role != "author":
        return "Access denied", 403

    posts = Post.query.filter_by(user_id=current_user.id).all()
    # Using a specific template for author dashboard
    return render_template("author_dashboard.html", posts=posts)


@app.route("/user_dashboard")
@login_required
def user_dashboard():
    # User dashboard now shows ALL posts as a feed
    posts = Post.query.order_by(Post.date.desc()).all()

    if current_user.role == "user":
        return render_template("user_dashboard.html", posts=posts)
    else:
        return redirect("/")


@app.route("/post/<int:id>")
@login_required
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template("post_detail.html", post=post)


# CREATE POST

@app.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    if current_user.role != "author":
        return "Only authors can create", 403

    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        post = Post(title=title, content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()

        return redirect("/author_dashboard")

    return render_template("create_post.html", form=form)


# DELETE POST

@app.route("/delete/<int:id>")
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)

    # author can delete own post OR admin
    if current_user.id == post.user_id or current_user.role == "admin":
        db.session.delete(post)
        db.session.commit()

        # Redirect back to appropriate dashboard
        if current_user.role == "admin":
            return redirect("/admin_dashboard")
        elif current_user.role == "author":
            return redirect("/author_dashboard")

    return redirect("/")


@app.route("/delete_user/<int:id>")
@login_required
def delete_user(id):
    if current_user.role != "admin":
        return "Access denied", 403

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/admin_dashboard")
