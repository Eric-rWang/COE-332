import json
import random

with open ('animals.json', 'r') as f:
	animals = json.load(f)
	rand_animal = random.randint(0, len(animals['animals']) - 1)
	print(json.dumps(animals['animals'][rand_animal], indent = 2))