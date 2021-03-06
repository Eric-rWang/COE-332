import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/helloworld', methods=['GET'])
def hello_world():
	return "Hello world\n"

@app.route('/specific', methods=['GET'])
def get_specific():
	head = request.args.get('head')
	body = request.args.get('body')
	arms = request.args.get('arms')
	legs = request.args.get('legs')
	tails = request.args.get('tails')
	
	result = get_specific_animals(head, body, arms, legs, tails)

	return json.dumps(result['animals'], indent = 2)

@app.route('/animals', methods=['GET'])
def get_animals():
	return json.dumps(get_data(), indent = 2)

def get_data():
	with open("animals.json", 'r') as json_file:
		userdata = json.load(json_file)
	return userdata

def get_specific_animals(head, body, arms, legs, tails):
	animal_data = get_data()
	result = {}
	result['animals'] = []
	
	if head is not None:
		for i in range(len(animal_data['animals'])):
			if animal_data['animals'][i]['head'] == head:
				result['animals'].append(animal_data['animals'][i])

	if body is not None:
		for i in reversed(range(len(result['animals']))):
			if result['animals'][i]['body'] != body:
				del result['animals'][i]

	if arms is not None:
		for i in reversed(range(len(result['animals']))):
			if result['animals'][i]['arms'] != arms:
				del result['animals'][i]

	if legs is not None:
		for i in reversed(range(len(result['animals']))):
			if result['animals'][i]['legs'] != legs:
				del result['animals'][i]

	if tails is not None:
		for i in reversed(range(len(result['animals']))):
			if result['animals'][i]['tails'] != tails:
				del result['animals'][i]

	return result

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')








