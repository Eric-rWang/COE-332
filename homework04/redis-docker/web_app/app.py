import json, petname, random, datetime, redis, uuid
from flask import Flask, request

app = Flask(__name__)

# test 
@app.route('/helloworld', methods=['GET'])
def hello_world():
	return 'Hello world 1\n'

# returns all animals
@app.route('/all_animals', methods=['GET'])
def print_animals():
	animal_data = get_data()
	return animal_data

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
		date_temp = str(animal_data['animals'][i]['created_on']).split()[0].split('-')
		date_animal = datetime.datetime(int(date_temp[0]), int(date_temp[1]), int(date_temp[2]))
		if date_animal >= start_date and date_animal <= end_date:
			query_animal["animals"].append(animal_data['animals'][i])

	#with open('animals_query.json', 'w') as out:
	#	json.dump(query_animal, out, indent = 2)

	#rd.set('query_animal', json.dumps(query_animal, indent = 2))

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

			rd.set('animals', json.dumps(animal_data, indent = 2))

			#with open('animals.json', 'w') as out:
			#	json.dump(animal_data, out, indent = 2)

			return animal_data['animals'][i]
			
	return 'Not updated\n'

# deletes animals within given date range
@app.route('/delete', methods=['GET'])
def delete_range():
	s = request.args.get('start').split('-')
	e = request.args.get('end').split('-')
	start_date = datetime.datetime(int(s[0]), int(s[1]), int(s[2]))
	end_date = datetime.datetime(int(e[0]), int(e[1]), int(e[2]))

	animal_data = get_data()
	animal_range = {"animals":[]}

	for i in range(len(animal_data['animals'])):
		date_temp = str(animal_data['animals'][i]['created_on']).split()[0].split('-')
		date_animal = datetime.datetime(int(date_temp[0]), int(date_temp[1]), int(date_temp[2]))
		if date_animal < start_date or date_animal > end_date:
			animal_range['animals'].append(animal_data['animals'][i])

	#with open('animals.json', 'w') as out:
	#	json.dump(animal_range, out, indent = 2)

	rd.set('animals', json.dumps(animal_range, indent = 2))

	return animal_range

# returns the average number of legs per animal
@app.route('/average_legs', methods=['GET'])
def average_legs():
	animal_data = get_data()
	total_animals = len(animal_data['animals'])
	legs = 0

	for i in range(len(animal_data['animals'])):
		legs += int(animal_data['animals'][i]['legs'])

	avg_legs = legs / total_animals

	return str(avg_legs) + '\n'

# returns total count of animals
@app.route('/total_animals', methods=['GET'])
def total_animals():
	animal_data = get_data()
	return str(len(animal_data['animals'])) + '\n'

@app.route('/reset', methods=['GET'])
def reset():
	animal_data = {"animals":[]}

	for animals in range(100):
		arms, legs = rand_arms(), rand_legs()
		animal_data['animals'].append({
			'uid': str(uuid.uuid4()),
			'created_on': str(datetime.datetime.now()),
			'head': rand_head(),
			'body': rand_body(),
			'arms': arms,
			'legs': legs,
			'tails': num_tails(arms, legs)
		})


	rd.set('animals', json.dumps(animal_data, indent = 2))

	return 'Reset!'
	
@app.route('/create', methods=['GET'])
def create():
	animal_data = get_data()

	for animals in range(100):
		arms, legs = rand_arms(), rand_legs()
		animal_data['animals'].append({
			'uid': str(uuid.uuid4()),
			'created_on': str(datetime.datetime.now()),
			'head': rand_head(),
			'body': rand_body(),
			'arms': arms,
			'legs': legs,
			'tails': num_tails(arms, legs)
		})

	rd.set('animals', json.dumps(animal_data, indent = 2))

	return 'Created!'

# dictionary for head types
head = {
	0: 'snake', 
	1: 'bull', 
	2: 'lion', 
	3: 'raven', 
	4: 'bunny'
}

# returns random head type
def rand_head():
	return head[random.randint(0, 4)]

# returns random body type using petname library
def rand_body():
	return petname.name() + "-" + petname.name()

# returns random number of arms
def rand_arms():
	return random.randrange(2, 11, 2)

# returns random number of legs
def rand_legs():
	return random.randrange(3, 13, 3)

# returns arms + legs for number of tails
def num_tails(arms, legs):
	return arms + legs

# returns useable data
def get_data():
	userdata = json.loads(rd.get('animals').decode('utf-8'))
	#with open("animals.json", 'r') as json_file:
	#	userdata = json.load(json_file)
	return userdata

if __name__ == '__main__':
	rd = redis.StrictRedis(host='redis', port=6379, db=0)
	app.run(debug=True, host='0.0.0.0')











