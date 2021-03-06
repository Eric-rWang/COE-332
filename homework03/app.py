import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def hello_world():
	return "Hello world\n"

@app.route('/specific', methods=['GET'])
def get_specific():
	return ''

@app.route('/animals', methods=['GET'])
def get_animals():
	return json.dumps(get_data())

def get_data():
	with open('animals.json', '-r') as json_file:
		userdata = json.load(json_file)
	return userdata

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')