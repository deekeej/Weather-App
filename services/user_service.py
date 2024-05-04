import hashlib
from database.database import db, User
from flask import session

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(login, password):
    user = User.query.filter((User.username == login) | (User.email == login)).first()
    if user and user.password_hash == hash_password(password):
        session['username'] = user.username  # Set the username in session
        return True
    return False

def register_user(username, email, password):
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return False  # User already exists
    new_user = User(username=username, email=email, password_hash=hash_password(password))
    db.session.add(new_user)
    db.session.commit()
    return True