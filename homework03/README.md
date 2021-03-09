# Animal Json-Parser with Flask
## Table of contents
* [General info](#general-info)
* [Functions](#functions)
* [Setup](#setup)
* [Flask](#flask)

## General info
Animals Json-Parser can generate random animal json files  with generate_animals.py and parse through them using read_animals. The file generate_animals.py will output a json file containing 20 animals with randomly generated attibutes. The read-animals.py file can parse through the animals json file and has the function breed(parent1, parent2) which takes properties from both parents and combines them, making a child. Lastly, test_read_animals.py tests the functions which breed uses.

## Functions
read-animals.py has the following functions:
* child_body(parent1, parent2): Combines the parent's body properties.
* child_arms(parent1, parent2): Adds and uses floor division to get number of arms.
* child_legs(parent1, parent2): Adds and uses floor division to get number of legs.
* child_tails(arms, legs): Adds the arms and legs to get number of tails.
* breed(parent1, parent2): Uses the functions above and creates a animal child json.

test_read-animals.py tests the functions stated above in read-animals.py.

## Setup
### How to download and run scripts directly
Before downloading make sure to have python3 installed as well as the petname library installed.
```
$ git clone https://github.com/Eric-rWang/COE-332.git
$ cd COE-332/homework02/
$ pip install petname
```
To run the scripts generate_animals.py, read_animals.py and test_read_animals.py run the following lines of code respectively.
```
$ python3 generate_animals.py animals.json
$ python3 read_animals.py animals.json
$ python3 test_read_animals.py
```
animals.json can be renamed to more fitting json file name. generate_animals.py and read_animals.py both require a json file as a second input.

## Flask
### Routes
* /helloworld (test)
* /countAnimals (returns number of animals in data)
* /animals (returns all animals)
* /buildAnimal/random (generates a random animal)
* /specificAnimals?head=" "&body=" "&arms=" "&legs=" "&tails=" " (optional aditional query parameters)
* /buildAnimal?head=" "&body=" "&arms=" "&legs=" "&tails=" " (query parameters required)











