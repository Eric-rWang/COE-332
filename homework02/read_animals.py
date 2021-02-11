#!/usr/bin/env python3
import json
import random
import sys

def breed(animals):
	rand_animal1 = random.randint(0, len(animals['animals']) - 1)
	rand_animal2 = random.randint(0, len(animals['animals']) - 1)

	head = animals['animals'][rand_animal1]['head']
	body = animals['animals'][rand_animal2]['body']
	arms = animals['animals'][rand_animal1]['arms']
	legs = animals['animals'][rand_animal2]['legs']
	tails = arms + legs

	child = {
		'head': head,
		'body': body,
		'arms': arms,
		'legs': legs,
		'tails': tails
	}

	print('Parents:')
	print(json.dumps(animals['animals'][rand_animal1], indent = 2))
	print(json.dumps(animals['animals'][rand_animal2], indent = 2))
	print('Child:')
	print(json.dumps(child, indent = 2))

def main():
	with open (sys.argv[1], 'r') as f:
		animals = json.load(f)
		rand_animal = random.randint(0, len(animals['animals']) - 1)
		print(json.dumps(animals['animals'][rand_animal], indent = 2))

		breed(animals)

if __name__ == '__main__':
	main()












