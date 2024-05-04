from flask import Blueprint, request, jsonify
from services.measurement_service import (
    insert_measurement,
    get_last_measurement,
    get_last_x_measurements,
    delete_measurement_by_id,
    serialize_measurement
)

measurement_blueprint = Blueprint('measurement', __name__)

@measurement_blueprint.route('/measurements', methods=['POST'])
def add_measurement():
    data = request.get_json()
    success = insert_measurement(data)
    return jsonify(success=success), 201 if success else 400

@measurement_blueprint.route('/measurements/latest', methods=['GET'])
def latest_measurement():
    measurement = get_last_measurement()
    if measurement:
        return jsonify(serialize_measurement(measurement)), 200
    else:
        return jsonify({"message": "No measurements found"}), 404

@measurement_blueprint.route('/measurements/last/<int:x>', methods=['GET'])
def last_x_measurements(x):
    measurements = get_last_x_measurements(x)
    serialized_measurements = [serialize_measurement(m) for m in measurements]
    return jsonify(serialized_measurements), 200 if measurements else 404

@measurement_blueprint.route('/measurements/delete/<int:id>', methods=['DELETE'])
def delete_measurement(id):
    success = delete_measurement_by_id(id)
    return jsonify(success=success), 200 if success else 400