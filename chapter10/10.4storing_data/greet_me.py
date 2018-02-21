import json

file = 'username.json'

with open(file) as f_obj:
	username = json.load(f_obj)
	print("welcome back " + username)