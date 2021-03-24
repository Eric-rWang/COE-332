import json, petname, random, datetime
from flask import Flask, request

app = Flask(__name__)

# test 
@app.route('/helloworld', methods=['GET'])
def hello_world():
	return 'Hello world\n'

# querys dates
@app.route('/dates', methods=['GET'])
def query_date():
	s = request.args.get('start').split('-')
	e = request.args.get('end').split('-')
	start_date = datetime.datetime(int(s[0]), int(s[1]), int(s[2]))
	end_date = datetime.datetime(int(e[0]), int(e[1]), int(e[2]))

	animal_data = get_data()
	query_animal = {"animals":[]}

	for i in range(len(animal_data['animals'])):
		date_temp = str(animal_data['animals'][i]['timestamp']).split()[0].split('-')
		date_animal = datetime.datetime(int(date_temp[0]), int(date_temp[1]), int(date_temp[2]))
		if date_animal >= start_date and date_animal <= end_date:
			query_animal["animals"].append(animal_data['animals'][i])

	with open('animals_query.json', 'w') as out:
		json.dump(query_animal, out, indent = 2)

	return query_animal

# gets specific animal
@app.route('/select', methods=['GET'])
def select_uid():
	uid = request.args.get('uid')
	animal_data = get_data()

	for i in range(len(animal_data['animals'])):
		if str(animal_data['animals'][i]['uid']) == str(uid):
			return json.dumps(animal_data['animals'][i], indent = 2) + '\n'

	return 'Animal not found\n'

# updates specific animal's properties
@app.route('/update', methods=['GET'])
def update_animal():
	uid = request.args.get('uid')
	animal_data = get_data()

	head = request.args.get('head')
	body = request.args.get('body')
	arms = request.args.get('arms')
	legs = request.args.get('legs')
	tails = request.args.get('tails')

	for i in range(len(animal_data['animals'])):
		if str(animal_data['animals'][i]['uid']) == str(uid):
			if head is not None:
				animal_data['animals'][i]['head'] = head
			if body is not None:
				animal_data['animals'][i]['body'] = body
			if arms is not None:
				animal_data['animals'][i]['arms'] = arms
			if legs is not None:
				animal_data['animals'][i]['legs'] = legs
			if tails is not None:
				animal_data['animals'][i]['tails'] = tails

			with open('animals.json', 'w') as out:
				json.dump(animal_data, out, indent = 2)

			return animal_data['animals'][i]
			
	return 'Not updated\n'

# returns useable data
def get_data():
	with open("animals.json", 'r') as json_file:
		userdata = json.load(json_file)
	return userdata



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')











