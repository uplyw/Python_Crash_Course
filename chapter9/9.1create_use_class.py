# class Dog():
# 	"""一次模拟小狗的简单尝试"""
# 	def __init__(self, name, age):
# 		"""初始化属性name和age"""
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		"""模拟小狗被命令蹲下"""
# 		print(self.name.title() + " is now sitting")

# 	def roll_over(self):
# 		print(self.name.title() + " rolled over")

# my_dog = Dog('willie', 4)
# your_dog = Dog('lucy', 2)
# print('my dog name is ' + my_dog.name.title() + '.')
# print('my dog is ' + str(my_dog.age) + ' years old.')
# my_dog.sit()
# my_dog.roll_over()

# print('your dog name is ' + your_dog.name.title() + '.')
# print('your dog is ' + str(your_dog.age) + ' years old.')
# your_dog.sit()
# your_dog.roll_over()

class Restaurant():
	"""docstring for Resraurant"""
	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("we're " + self.restaurant_name.title() + " we sale " + self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name.title() + "'s open!")

restaurant = Restaurant('hhh','hot')
restaurant.describe_restaurant()
restaurant.open_restaurant()