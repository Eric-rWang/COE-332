# Animal Json-Parser
## Table of contents
* [General info](#general-info)
* [Functions](#functions)
* [Setup](#setup)

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
$ git clone git@github.com:Eric-rWang/COE-332.git
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

### How to build an image with Docker
Make sure to have docker installed before building the image.
Inside the homework02 folder run the following commands in terminal. Remember to replace dockerhubusername with personal docker username.
```
$ docker build -t dockerhubusername/json-parser:1.5 .
```
In order to run the scripts inside the container execute the following.
Run generate_animals.py (will generate a json file):
```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) dockerhubusername/json-parser:1.5 generate_animals.py /data/animals.json
```
Run read_animals.py:
```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) dockerhubusername/json-parser:1.5 read_animals.py /data/animals.json
```
Run test_read_animals.py (unit tests for read_animals.py):
```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) dockerhubusername/json-parser:1.5 test_read_animals.py
```










