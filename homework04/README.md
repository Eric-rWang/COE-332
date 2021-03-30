# Animal Json-Parser with Flask, Redis and Docker-Compose
## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Flask](#flask)

## General info
This Docker Compose app utilizes Redis databases and Flask to create routes that when
accessed will return specific animal data or create/delete/update given their uid, 
created dates. The Redis database stores 100 animals allowing the user to access the
data using the provided Flask routes. It can also reset the data, creating a new set
or data or creating new animals added onto the original dataset. 

## Setup
### How to download and run
First clone the repository and find the folder redis-docker within the homework04
folder.
```
$ git clone https://github.com/Eric-rWang/COE-332.git
$ cd COE-332/homework04/redis-docker
```
Before starting docker-compose, make sure to build it to ensure it is up to date.
```
$ docker-compose build --no-cashe
```
To run the app, run the following.
```
$ docker-compose up -d
```
And to check both services, Redis and Flask, are up and running.
```
$ docker-compose ps
```
Both of the services should say up.
Once up the user can use the following routes.

* localhost:5000/helloworld (test)
* localhost:5000/all_animals (returns all animals)
* localhost:5000/dates?start=''&end='' (returns animals created within the dates)
* localhost:5000/select?uid='' (returns specific animals with uid)
* localhost:5000/update?uid=''&head=''&body&''&arms=''&legs=''&tails='' (updates specified animals)
* localhost:5000/delete?start=''&end='' (deletes animals created within the dates)
* localhost:5000/total_animals (returns total number of animals)
* localhost:5000/reset (resets animals in redis database)

## Flask
### Routes
* /helloworld (test)
* /all_animals (returns all animals)
* /dates?start=''&end='' (returns animals created within the dates)
* /select?uid='' (returns specific animals with uid)
* /update?uid=''&head=''&body&''&arms=''&legs=''&tails='' (updates specified animals)
* /delete?start=''&end='' (deletes animals created within the dates)
* /average_legs (returns the average number of legs)
* /total_animals (returns total number of animals)
* /reset (resets animals in redis database)











