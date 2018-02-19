# 传递任意数量的实参
# def make_pizza(*toppings):
# 	print(toppings)
# make_pizza('pepproni')
# make_pizza('apple','banana','orange')

# def make_pizza(*toppings):
# 	print('\nmakeing a pizza with following toppings:')
# 	for topping in toppings:
# 		print(' - ' + topping)
# make_pizza('pepproni')
# make_pizza('apple','banana','orange')

# def make_pizza(size,*toppings):
# 	print('\nmakeing a ' + str(size) + '-inch pizza with following toppings:')
# 	for topping in toppings:
# 		print(' - ' + topping)
# make_pizza(12,'pepproni')
# make_pizza(24,'apple','banana','orange')

# def build_profile(first,last,**user_info):
# 	profile = {}
# 	profile['first_name'] = first
# 	profile['last_name'] = last
# 	for key,value in user_info.items():
# 		profile[key] = value
# 	return profile
# user_profile = build_profile('li', 'lei',age = 18,sex = 'man')
# print(user_profile)

#练习

# def fruits(*class_name):
# 	print(class_name)
# fruits('apple','banana','orange','kiwi')

def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
hahaha = build_profile('li', 'lei', age = 24, sex = 'man', city = 'huizhou')
print(hahaha)