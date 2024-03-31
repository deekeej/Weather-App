# controllers/api_routes_measurement.py
from flask import Blueprint, request, jsonify
from services.measurement_service import insert_measurement, get_last_measurement,get_last_x_measurements, delete_measurement_by_timestamp

measurement_blueprint = Blueprint('measurement', __name__)

@measurement_blueprint.route('/measurements', methods=['POST'])
def add_measurement():
    data = request.get_json()
    # Assume insert_measurement function exists which saves data to a database
    success = insert_measurement(data)
    return jsonify(success=success), 201 if success else 400

@measurement_blueprint.route('/measurements/latest', methods=['GET'])
def latest_measurement():
    # Assume get_last_measurement function exists which retrieves data from a database
    measurement = get_last_measurement()
    return jsonify(measurement), 200 if measurement else 404

@measurement_blueprint.route('/measurements/last/<int:x>', methods=['GET'])
def last_x_measurements(x):
    # Assume get_last_x_measurements function exists which retrieves data from a database
    measurements = get_last_x_measurements(x)
    return jsonify(measurements), 200 if measurements else 404

@measurement_blueprint.route('/measurements/delete/<string:timestamp>', methods=['DELETE'])
def delete_measurement(timestamp):
    # Assume delete_measurement_by_timestamp function exists which deletes data by timestamp
    success = delete_measurement_by_timestamp(timestamp)
    return jsonify(success=success), 200 if success else 400
