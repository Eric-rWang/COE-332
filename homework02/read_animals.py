#!/usr/bin/env python3
import json
import random
import sys

def main():
	with open ('animals.json', 'r') as f:
		animals = json.load(f)
		rand_animal = random.randint(0, len(animals['animals']) - 1)
		print(json.dumps(animals['animals'][rand_animal], indent = 2))

if __name__ == '__main':
	main()