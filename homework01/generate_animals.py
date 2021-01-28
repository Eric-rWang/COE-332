# ERIC WANG (erw825)
# generating random animals and writing to json

import json
import petname
import random

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
	return petname.generate(words=2, separator='-', letters=6)

# returns random number of arms
def rand_arms():
	return random.randrange(2, 11, 2)

# returns random number of legs
def rand_legs():
	return random.randrange(3, 13, 3)

# returns arms + legs for number of tails
def num_tails(arms, legs):
	return arms + legs

data = {}
data['animals'] = []

# generating 20 animals
for animals in range(20):
	arms, legs = rand_arms(), rand_legs()
	data['animals'].append({
		'head': rand_head(),
		'body': rand_body(),
		'arms': arms,
		'legs': legs,
		'tails': num_tails(arms, legs)
	})

# opening/creating file to write to
with open('animals.json', 'w') as out:
	json.dump(data, out, indent = 2)








