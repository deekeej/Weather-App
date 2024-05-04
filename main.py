from flask import Flask
from database.database import db
from controllers.site_routes import site_blueprint
from controllers.api_routes_user import auth_blueprint
from controllers.api_routes_measurement import measurement_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# Register the API blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(measurement_blueprint, url_prefix='/api')
app.register_blueprint(site_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
