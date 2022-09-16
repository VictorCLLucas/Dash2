from crypt import methods
from flask import Flask
from flask_restful import Api
from flask_cors import cross_origin

import external_calls as ext
from server import requires_auth

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def home():
		resp = app.make_response('Hello World!')
		resp.headers["Access-Control-Allow-Origin"] = "*"
		return resp


@app.route("/boredapi", methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def get_bored_api():
	bored_api_data = ext.get_bored_data()
	resp = app.make_response(bored_api_data)
	resp.headers["Access-Control-Allow-Origin"] = "*"
	return resp



if __name__ == "__main__":
		app.run(debug=True)
