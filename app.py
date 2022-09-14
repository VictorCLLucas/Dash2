from crypt import methods
from flask import Flask
from flask_restful import Api, Resource

import external_calls as ext


app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
		resp = app.make_response('Hello World!')
		resp.headers["Access-Control-Allow-Origin"] = "*"
		return resp


@app.route("/boredapi", methods=['GET'])
def get_bored_api():
	bored_api_data = ext.get_bored_data()
	resp = app.make_response(bored_api_data)
	resp.headers["Access-Control-Allow-Origin"] = "*"
	return resp



if __name__ == "__main__":
		app.run(debug=True)
		