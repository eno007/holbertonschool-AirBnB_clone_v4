#!/usr/bin/python3
''' *** *** '''
from os import getenv
from flask import Flask, make_response
from models import storage
from api.v1.views import app_views
from flask import jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def close(self):
    ''' *** *** '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' *** *** '''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    ''' *** *** '''
    
    env_host = getenv('HBNB_API_HOST', '0.0.0.0')
    env_port = getenv('HBNB_API_PORT', 5000)
    app.run(host=env_host, port=env_port, threaded=True)
    