import json, petname, random
from flask import Flask, request

app = Flask(__name__)

# test 
@app.route('/helloworld', methods=['GET'])
def hello_world():
	return "Hello world\n"

# querys dates
@app.route('/dates', method=['GET'])
def query_date():
	
	return ''

# gets specific animal
@app.route('/select', method=['GET'])
def select_uid():
	uid = request.args.get('uid')
	animal_data = get_data()

	for i in range(len(animal_data['animals'])):
		if str(animal_data['animals'][i]['uid']) == str(uid):
			return json.dumps(animal_data['animals'][i], indent = 2) + '\n'

	return 'Animal not found'

# updates specific animal's properties
@app.route('/update', method=['GET'])
def update_animal():
	uid = request.args.get('uid')
	head = request.args.get('head')
	body = request.args.get('body')
	arms = request.args.get('arms')
	legs = request.args.get('legs')
	tails = request.args.get('tails')

# returns useable data
def get_data():
	with open("animals.json", 'r') as json_file:
		userdata = json.load(json_file)
	return userdata















