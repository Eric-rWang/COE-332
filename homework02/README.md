# Animal Json-Parser
## Table of contents
* [General info](#general-info)
* [Functions](#functions)
* [Setup](#setup)

## General info
Animals Json-Parser can generate random animal json files  with generate_animals.py and parse through them using read_animals. The file generate_animals.py will output a json file containing 20 animals with randomly generated attibutes. The read-animals.py file can parse through the animals json file and has the function breed(parent1, parent2) which takes properties from both parents and combines them, making a child. Lastly, test_read_animals.py tests the functions which breed uses.

## Functions
read-animals.py has the following functions:
* child_body(parent1, parent2): Combines the parent's body properties
* child_arms(parent1, parent2): Adds and uses floor division to get number of arms
* child_legs(parent1, parent2): Adds and uses floor division to get number of legs
* child_tails(arms, legs): Adds the arms and legs to get number of tails
* breed(parent1, parent2): Uses the functions above and creates a animal child json

test_read-animals.py tests the functions stated above in read-animals.py

## Setup
### How to download and run scripts directly
$ git clone git@github.com:Eric-rWang/COE-332.git