from flask import Blueprint, request, redirect, url_for, render_template
from services.user_service import login_user, register_user

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if login_user(username, password):
           return redirect(url_for('site.dashboard'))
        error_message = "Invalid username or password."
    return render_template('login.html',error_message=error_message)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            error_message = "Passwords do not match."
        elif not register_user(username, email, password):
            error_message = "User with this username or email already exists."
        else:
            return redirect(url_for('auth.login'))
    return render_template('register.html', error_message=error_message)

@auth_blueprint.route('/logout')
def logout():
    return redirect(url_for('site.index'))