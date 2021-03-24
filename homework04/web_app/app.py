import json, petname, random
from flask import Flask, request

app = Flask(__name__)

# test 
@app.route('/helloworld', methods=['GET'])
def hello_world():
	return 'Hello world\n'

# querys dates
@app.route('/dates', methods=['GET'])
def query_date():
	start_date = request.args.get('start')
	end_date = request.args.get('end')
	
	return 'h\n'

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











