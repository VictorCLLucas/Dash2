from crypt import methods
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])

def home():
    return 'Hello world!'

if __name__ == "__main__":
    app.run(debug=True)
    