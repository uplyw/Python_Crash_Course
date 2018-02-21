# import json

# username = input("what's your name?")
# file = 'username.json'
# with open(file,'w') as f_obj:
# 	json.dump(username, f_obj)
# 	print("we'll remember you when you come back, " + username)


# 合并 remember_me.py  和  greet_me.py


# import json

# filename = 'username.json'

# try:
# 	with open(filename) as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	username = input("what's your name?")
# 	with open(filename,'w') as f_obj:
# 		json.dump(username, f_obj)
# 		print("we'll remember you," + username)
# else:
# 	print("welcome back " + username)


# 重构 remember_me.py


# import json
# def greet_user():
# 	filename = 'username.txt'
# 	try:
# 		with open(filename) as f_obj:
# 			username = json.load(f_obj)
# 	except FileNotFoundError:
# 		username = input("what's you name?")
# 		with open(filename,'w') as f_obj:
# 			json.dump(username, f_obj)
# 			print("we'll remember you, " + username)
# 	else:
# 		print('welcome back ' + username)

# greet_user()



#再重构

# import json

# def get_stored_username():
# 	filename = 'username.json'
# 	try:
# 		with open(filename) as f_obj:
# 			username = json.load(f_obj)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return username

# def greet_user():
# 	username = get_stored_username()
# 	if username:
# 		print("welcome back "+username)
# 	else:
# 		username = input("what's your name?")
# 		filename = 'username.json'
# 		with open(filename,'w') as f_obj:
# 			json.dump(username, f_obj)
# 			print("we'll remember you " + username)
# greet_user()


# 再再重构

import json
def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_user():
	username = input("what's you name?")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		print("welcome back "+ username)
	else:
		username = get_new_user()
		print("we'll remember you " + username)

greet_user()

