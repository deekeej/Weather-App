# services/measurement_service.py
from datetime import datetime
# Importing the mock database
from database.database import measurements

def insert_measurement(data):
    """
    Inserts a new measurement into the mock database.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    temp = data['temp']
    measurement = {"timestamp": timestamp, "temp": temp}
    measurements.append(measurement)
    return True

def get_last_measurement():
    """
    Retrieves the last measurement from the mock database.
    """
    if measurements:
        return measurements[-1]
    else:
        return None

def get_last_x_measurements(x):
    """
    Retrieves the last X measurements from the mock database.
    """
    return measurements[-x:] if x <= len(measurements) else measurements

def delete_measurement_by_timestamp(timestamp):
    """
    Deletes a measurement by its timestamp from the mock database.
    """
    global measurements  # Reference the global variable if you are using a simple list for storage
    # Find the index of the measurement to delete
    index_to_delete = next((index for (index, m) in enumerate(measurements) if m["timestamp"] == timestamp), None)

    if index_to_delete is not None:
        del measurements[index_to_delete]
        return True
    else:
        return False
