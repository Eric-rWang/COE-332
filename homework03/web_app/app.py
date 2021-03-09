import json
import petname
import random
from flask import Flask, request

app = Flask(__name__)

# test 
@app.route('/helloworld', methods=['GET'])
def hello_world():
	return "Hello world\n"

@app.route('/countAnimals', methods=['GET'])
def get_animals_count():
	animal_data = get_data()
	return str(len(animal_data['animals'])) + '\n'

@app.route('/specificAnimals', methods=['GET'])
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

@app.route('/buildAnimal/random', methods=['GET'])
def create_animal():
	animal = {}
	animal['animals'] = []
	head = {
		0: 'snake', 
		1: 'bull', 
		2: 'lion', 
		3: 'raven', 
		4: 'bunny'
	}
	arms = random.randrange(2, 11, 2)
	legs = random.randrange(3, 13, 3)
	animal['animals'].append({
		'head': head[random.randint(0, 4)],
		'body': petname.name() + "-" + petname.name(),
		'arms': arms,
		'legs': legs,
		'tails': arms + legs
	})

	return json.dumps(animal['animals'][0], indent = 2) + '\n'

@app.route('/buildAnimal', methods=['GET'])
def create_specific_animal():
	animal = {}
	animal['animals'] = []
	animal['animals'].append({
		'head': request.args.get('head'),
		'body': request.args.get('body'),
		'arms': int(request.args.get('arms')),
		'legs': int(request.args.get('legs')),
		'tails': int(request.args.get('tails'))
	})

	return json.dumps(animal['animals'][0], indent = 2) + '\n'

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
			if str(animal_data['animals'][i]['head']) == str(head):
				result['animals'].append(animal_data['animals'][i])

	if body is not None:
		for i in reversed(range(len(result['animals']))):
			if str(result['animals'][i]['body']) != str(body):
				del result['animals'][i]

	if arms is not None:
		for i in reversed(range(len(result['animals']))):
			if str(result['animals'][i]['arms']) != str(arms):
				del result['animals'][i]

	if legs is not None:
		for i in reversed(range(len(result['animals']))):
			if str(result['animals'][i]['legs']) != str(legs):
				del result['animals'][i]

	if tails is not None:
		for i in reversed(range(len(result['animals']))):
			if str(result['animals'][i]['tails']) != str(tails):
				del result['animals'][i]

	return result

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')








