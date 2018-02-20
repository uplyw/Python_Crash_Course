# class Car():
# 	"""一次模拟汽车的简单尝试"""

# 	def __init__(self, make, model, year):
# 		"""初始化描述汽车的属性"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		"""返回整洁的描述性信息"""
# 		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return long_name.title()

# 	def read_odometer(self):
# 		print('this car has ' + str(self.odometer_reading) + ' miles on it')

# my_new_car = Car('audi', 'a4', 2018)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# class Car():
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		descriptive = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return descriptive

# 	def read_odometer(self):
# 		print('this car has ' + str(self.odometer_reading) + ' miles on it')

# 	def update_odometer(self,miles):
# 		self.odometer_reading = miles
# 		if miles >= self.odometer_reading:
# 			self.odometer_reading = miles
# 		else:
# 			print('you cant')
# my_new_car = Car('audi', 'a4', 2018)
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


# class Car():
# 	"""docstring for Car"""
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.read_odometer = 0

# 	def car_info(self):
# 		car_i = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return car_i

# 	def car_odom(self):
# 		print('the car is ' + str(self.read_odometer))

# 	def revise_car_odom(self,milage):
# 		self.read_odometer = milage
# 		if milage >= self.read_odometer:
# 			self.read_odometer = milage
# 		else:
# 			print("you can't")

# 	def up_car_odom(self,num):
# 		self.read_odometer += num

# my_new_car = Car('audi','a4',2018)
# print(my_new_car.car_info())
# my_new_car.car_odom()
# my_new_car.revise_car_odom(23500)
# my_new_car.car_odom()
# my_new_car.up_car_odom(200)
# my_new_car.car_odom()
# my_new_car.revise_car_odom(100)
# my_new_car.car_odom()


#练习
class User():
	
	def __init__(self, first_name, last_name, age, sex):
		"""定义用户属性"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.sex = sex
		self.login_attempts = 1

	def describe_user(self):
		"""打印用户摘要"""
		if self.sex == "man":
			ta = "he"
		else:
			ta = "she"
		user_info = self.first_name + " " + self.last_name + "," + ta + " is " + str(self.age) + " is " + self.sex + "."
		return user_info

	def greet_user(self):
		"""个性问候用户"""
		print("hello," + self.first_name + " " + self.last_name)

	def increment_login_attments(self,attempt):
		self.login_attempts += attempt
		print(self.login_attempts)

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(self.login_attempts)
one_user = User('li', 'lei', 12, "man")
print(one_user.describe_user())
one_user.greet_user()

two_user = User('han','meimei',13,'woman')
print(two_user.describe_user())
two_user.greet_user()
one_user.increment_login_attments(1)
one_user.increment_login_attments(1)
one_user.increment_login_attments(1)
one_user.increment_login_attments(1)
one_user.reset_login_attempts()