# 🔐 Flask Authentication System Guide

## Overview
Your Flask application now has a complete user authentication system with login, registration, and session management.

## Features Implemented

### ✅ User Registration
- New users can create accounts with username and password
- Password confirmation validation
- Passwords are securely hashed using Werkzeug's security functions
- Username uniqueness check

### ✅ User Login
- Secure login with username and password
- Password verification using hash comparison
- Session management with Flask-Login
- Automatic redirect to dashboard after login

### ✅ User Logout
- Secure logout functionality
- Session clearing
- Redirect to home page

### ✅ Protected Routes
- Dashboard is now protected (login required)
- Unauthorized users are redirected to login page
- Flash messages for user feedback

### ✅ Navigation Bar Updates
- Shows Login/Register buttons for guests
- Shows username and Logout button for authenticated users
- Dynamic content based on authentication status

## How to Use

### 1. Start the Flask Application
```bash
cd "Day 15/flask"
/Users/ragnar/Documents/COD\ LANG/FTW/.venv/bin/python main.py
```

### 2. Access the Application
Open your browser and go to: `http://localhost:5001`

### 3. Register a New Account
1. Click "Register" in the navigation bar
2. Enter a username (minimum 3 characters)
3. Enter a password (minimum 6 characters)
4. Confirm your password
5. Click "Register"
6. You'll be redirected to the login page

### 4. Login
1. Click "Login" in the navigation bar
2. Enter your username and password
3. Click "Login"
4. You'll be redirected to the dashboard

### 5. Access Protected Dashboard
- The dashboard now shows your username: "Welcome to the Dashboard, [username]!"
- Only logged-in users can access it
- Try accessing `/dashboard` without logging in - you'll be redirected to login

### 6. Logout
- Click "Logout" in the navigation bar
- Your session will be cleared
- You'll be redirected to the home page

## Code Structure

### main.py
- **Flask-Login integration**: Manages user sessions
- **User class**: Simple user model with UserMixin
- **users_db**: In-memory dictionary storing users (for demo purposes)
- **Password hashing**: Secure password storage using `generate_password_hash()`
- **Password verification**: Using `check_password_hash()`
- **@login_required decorator**: Protects routes

### Templates
- **base.html**: Main template with flash message support
- **login.html**: Login form
- **register.html**: Registration form
- **dashboard.html**: Protected page showing username
- **nav.html**: Dynamic navigation with auth status

## Security Features

1. **Password Hashing**: Passwords are never stored in plain text
2. **Session Management**: Flask-Login manages secure sessions
3. **CSRF Protection**: Built into Flask forms (can be enhanced with Flask-WTF)
4. **Route Protection**: `@login_required` decorator prevents unauthorized access
5. **Password Validation**: Minimum length requirements
6. **Flash Messages**: User feedback for all actions

## Important Notes

⚠️ **Current Limitations (Development Mode)**:
- Users are stored in memory (lost on server restart)
- Secret key is hardcoded (change for production)
- No email verification
- No password reset functionality
- No "Remember Me" feature

## Upgrading to Production

To make this production-ready, you should:

1. **Use a Database** (SQLite, PostgreSQL, MySQL):
   ```python
   # Install Flask-SQLAlchemy
   pip install flask-sqlalchemy
   
   # Create User model with database
   from flask_sqlalchemy import SQLAlchemy
   db = SQLAlchemy(app)
   ```

2. **Change Secret Key**:
   ```python
   import secrets
   app.secret_key = secrets.token_hex(16)
   # Or use environment variable
   app.secret_key = os.environ.get('SECRET_KEY')
   ```

3. **Add Flask-WTF** for better form handling:
   ```bash
   pip install flask-wtf
   ```

4. **Add Email Verification**
5. **Add Password Reset Feature**
6. **Add "Remember Me" checkbox**
7. **Use HTTPS in production**

## Testing the Authentication

### Test Scenario 1: Registration
1. Go to `http://localhost:5001/register`
2. Register with username: `testuser` and password: `password123`
3. Should see success message and redirect to login

### Test Scenario 2: Login
1. Go to `http://localhost:5001/login`
2. Login with credentials from above
3. Should redirect to dashboard with personalized greeting

### Test Scenario 3: Protected Route
1. Logout if logged in
2. Try to access `http://localhost:5001/dashboard` directly
3. Should redirect to login page with message

### Test Scenario 4: Invalid Login
1. Try logging in with wrong password
2. Should see error message: "Invalid username or password!"

## Flash Message Categories

The app uses Bootstrap alert classes:
- `success` (green): Successful operations
- `danger` (red): Errors
- `info` (blue): Informational messages

## Questions?

Common issues:
- **"No module named 'flask_login'"**: Run the install command again
- **Users disappear after restart**: This is expected with in-memory storage
- **Can't access dashboard**: Make sure you're logged in

Enjoy your new authentication system! 🎉
