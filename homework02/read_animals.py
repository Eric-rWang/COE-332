#!/usr/bin/env python3
import json
import random
import sys

def child_body(parent1, parent2):
	return parent1[0] + '-' + parent2[1]

def child_arms(parent1, parent2):
	return (parent1 + parent2) // 2

def child_legs(parent1, parent2):
	return (parent1 + parent2) // 2

def child_tails(arms, legs):
	return arms + legs

def breed(parent1, parent2):

	p1 = json.loads(parent1)
	p2 = json.loads(parent2)

	arms = child_arms(p1['arms'], p2['arms'])
	legs = child_legs(p1['legs'], p2['legs'])
	
	child = {
		'head': p1['head'],
		'body': child_body(p1['body'].split('-'), p2['body'].split('-')),
		'arms': arms,
		'legs': legs,
		'tails': child_tails(arms, legs)
	}

	print(child_body(p1, p2))

	print('Parents:')
	print(parent1)
	print(parent2)
	print('Child:')
	print(json.dumps(child, indent = 2))

def main():
	with open (sys.argv[1], 'r') as f:
		animals = json.load(f)
		rand_animal = random.randint(0, len(animals['animals']) - 1)
		print(json.dumps(animals['animals'][rand_animal], indent = 2))

		rand_animal1 = random.randint(0, len(animals['animals']) - 1)
		rand_animal2 = random.randint(0, len(animals['animals']) - 1)

		parent1 = json.dumps(animals['animals'][rand_animal1], indent = 2)
		parent2 = json.dumps(animals['animals'][rand_animal2], indent = 2)

		breed(parent1, parent2)

if __name__ == '__main__':
	main()












