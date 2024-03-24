from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data
measurements = [
    {"timestamp": "2024-03-28 12:00", "temp": -6},
    {"timestamp": "2024-03-24 09:00", "temp": 23},
    {"timestamp": "2024-03-23 10:00", "temp": 22.5},
    {"timestamp": "2024-03-23 10:00", "temp": 2},
    {"timestamp": "2024-03-23 07:00", "temp": 12},
    # ... more measurements
]


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:num_last_measurements>', methods=['GET'])
def dashboard(num_last_measurements=5):
    latest_measurement = measurements[0]
    if request.method == 'POST':
        # If the form is submitted, update the number of measurements to display
        num_last_measurements = int(request.form.get('numRecords', num_last_measurements))
    last_measurements = measurements[:num_last_measurements]
    return render_template(
        'dashboard.html',
        latest_measurement=latest_measurement,
        last_measurements=last_measurements,
        num_last_measurements=num_last_measurements,
        username="User"
    )

""""
@app.route('/')
@app.route('/<int:num_last_measurements>')
def dashboard(num_last_measurements=5):  # Display last 5 measurements by default
    latest_measurement = measurements[0]
    last_measurements = measurements[:num_last_measurements]
    return render_template(
        'dashboard.html',
        latest_measurement=latest_measurement,
        last_measurements=last_measurements,
        num_last_measurements=num_last_measurements,
        username="User"
    )
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login here
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration here
        return redirect(url_for('dashboard'))
    return render_template('register.html')

# More routes and functions as needed...

if __name__ == '__main__':
    app.run(debug=True)
