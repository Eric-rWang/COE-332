#!/usr/bin/env python3
import json, random, sys, uuid, datetime

def child_body(parent1, parent2):
	if len(parent1) != 0 and len(parent2) != 0:
		return str(parent1).split('-')[0] + '-' + str(parent2).split('-')[1]
	else:
		raise IndexError('list index out of range')

def child_arms(parent1, parent2):
	if type(parent1) is int and type(parent2) is int:
		return (parent1 + parent2) // 2
	else:
		raise TypeError('variable not int')

def child_legs(parent1, parent2):
	if type(parent1) is int and type(parent2) is int:
		return (parent1 + parent2) // 2	
	else:
		raise TypeError('variable not int')

def child_tails(arms, legs):
	if type(arms) is int and type(legs) is int:
		return arms + legs
	else:
		raise TypeError('variable not int')

def breed(parent1, parent2):

	p1 = json.loads(parent1)
	p2 = json.loads(parent2)

	body1 = p1['body']
	body2 = p2['body']

	arms = child_arms(p1['arms'], p2['arms'])
	legs = child_legs(p1['legs'], p2['legs'])
	
	child = {
		'uid': str(uuid.uuid4()),
		'timestamp': str(datetime.datetime.now()), 
		'head': p1['head'],
		'body': child_body(body1, body2),
		'arms': arms,
		'legs': legs,
		'tails': child_tails(arms, legs)
	}

	print('Child:')
	print(json.dumps(child, indent = 2))

	return child

def main():
	with open (sys.argv[1], 'r') as f:
		animals = json.load(f)
		rand_animal = random.randint(0, len(animals['animals']) - 1)
		print(json.dumps(animals['animals'][rand_animal], indent = 2))

		rand_animal1 = random.randint(0, len(animals['animals']) - 1)
		rand_animal2 = random.randint(0, len(animals['animals']) - 1)

		print('Parents:')
		print(json.dumps(animals['animals'][rand_animal1], indent = 2))
		print(json.dumps(animals['animals'][rand_animal2], indent = 2))

		parent1 = json.dumps(animals['animals'][rand_animal1], indent = 2)
		parent2 = json.dumps(animals['animals'][rand_animal2], indent = 2)

		breed(parent1, parent2)

if __name__ == '__main__':
	main()












