import requests

response1 = requests.get(url="http://localhost:5000/countAnimals")
response2 = requests.get(url="http://localhost:5000/specificAnimals?head='bunny'")
response3 = requests.get(url="http://localhost:5000/animals")
response4 = requests.get(url="http://localhost:5000/buildAnimal/random")
response5 = requests.get(url="http://localhost:5000/buildAnimal?head='bunny'&body='gull-snail'&arms=10&legs=3&tails=13")

print(response1.status_code)
print(response1.json())
print(response1.headers)

print(response2.json(indent = 2))
print(response3.json(indent = 2))
print(response4.json(indent = 2))
print(response5.json(indent = 2))