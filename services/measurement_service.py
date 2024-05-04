from database.database import db, Data
from datetime import datetime

def serialize_measurement(measurement):
     return {
        "id": measurement.id,
        "temperature": measurement.temperature,
        "timestamp": measurement.timestamp.strftime('%Y-%m-%d %H:%M')
    }

def insert_measurement(data):
    # Generate a timestamp for the new measurement
    timestamp = datetime.now()
    temp = data['temp']
    measurement = Data(temperature=temp, timestamp=timestamp)
    db.session.add(measurement)
    db.session.commit()
    return True

def get_last_measurement():
    return Data.query.order_by(Data.timestamp.desc()).first()

def get_last_x_measurements(x):
    return Data.query.order_by(Data.timestamp.desc()).limit(x).all()

def delete_measurement_by_id(id):
    measurement = Data.query.get(id)
    if measurement:
        db.session.delete(measurement)
        db.session.commit()
        return True
    else:
        return False