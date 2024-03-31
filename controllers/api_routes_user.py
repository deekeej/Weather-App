from flask import Blueprint, request, redirect, url_for, render_template
from services.user_service import login_user, register_user

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if login_user(username, password):
           return redirect(url_for('site.dashboard'))
        else:
            return "Login failed", 401
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if register_user(username, email, password):
         return redirect(url_for('auth.login'))
        else:
            return "Registration failed", 400
    return render_template('register.html')
