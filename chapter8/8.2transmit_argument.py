# def describe_pet(animal_type,pet_name):
# 	'''显示宠物信息'''
# 	print('\nI have a ' + animal_type)
# 	print('my ' +  animal_type + "'s name is " + pet_name)
# describe_pet('hamster', 'harry')
# describe_pet('cat', 'marry')
# describe_pet('dog', 'lee')

# def describe_pet(animal_type,pet_name):
# 	'''显示宠物信息'''
# 	print('\nI have a ' + animal_type)
# 	print('my ' +  animal_type + "'s name is " + pet_name)
# describe_pet(pet_name = 'harry' , animal_type = 'hamster')

# def describe_pet(animal_type = 'dog' ,pet_name = 'lee'):
# 	'''显示宠物信息'''
# 	print('\nI have a ' + animal_type)
# 	print('my ' +  animal_type + "'s name is " + pet_name)
# # describe_pet( animal_type = 'hamster' , pet_name = 'harry')
# describe_pet()

# 练习
# def make_shirt(size,word):
# 	print('the shirt is ' + size)
# 	print('the shirt word is ' + word)
# make_shirt('24', 'hello')
# make_shirt(size = '28', word = '你好')

def make_shirt(size = '32',word = 'i love python'):
	print('the shirt is ' + size)
	print('the shirt word is ' + word)
make_shirt()
make_shirt(size = '28', word = '你好')