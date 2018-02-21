import json
def get_user_number():
	filename = 'user_number.json'
	try:
		with open(filename) as f_obj:
			user_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return user_number

def get_new_number():
	user_number = input("you like number:")
	filename = 'user_number.json'
	with open(filename,'w') as f_obj:
		json.dump(user_number, f_obj)
	return user_number

def show_number():
	user_number = get_user_number()
	if user_number:
		print("you like:" + user_number)
	else:
		user_number = get_new_number()
		print("we'll remember you like " + user_number)

show_number()