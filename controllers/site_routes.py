# site_routes.py
from flask import Blueprint, render_template
from services.measurement_service import (
    get_last_measurement,
    get_last_x_measurements,
)

site_blueprint = Blueprint('site', __name__)

@site_blueprint.route('/')
def index():
    return render_template('login.html')

@site_blueprint.route('/dashboard')
def dashboard():
    latest_measurement = get_last_measurement()
    last_measurements = get_last_x_measurements(5)  # For example, get the last 5
    num_last_measurements = len(last_measurements)

    return render_template(
        'dashboard.html',
        latest_measurement=latest_measurement,
        last_measurements=last_measurements,
        num_last_measurements=num_last_measurements,
    )
