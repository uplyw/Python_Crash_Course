import json

number = [2,3,5,7,11,13]

filename = 'number.json'
with open(filename, 'w') as n_obj:
	json.dump(number, n_obj)
