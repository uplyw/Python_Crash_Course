import json
file = 'number.json'
with open(file) as n_obj:
	numbers = json.load(n_obj)

print(numbers)