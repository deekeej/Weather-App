from flask import Flask,redirect,url_for
from controllers.site_routes import site_blueprint
from controllers.api_routes_user import auth_blueprint
from controllers.api_routes_measurement import measurement_blueprint

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(measurement_blueprint, url_prefix='/api')
app.register_blueprint(site_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
