# class Car():
# 	"""一次模拟汽车的简单尝试"""
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = str(self.year) + " " + self.make + " " + self.model
# 		return long_name

# 	def read_odometer(self):
# 		print("This car has " + str(self.odometer_reading) + " miles on it.")

# 	def update_odometer(self,mileage):
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")
		
# 	def increment_odometer(self,miles):
# 		self.odometer_reading += miles
# #继承父类
# class ElectricCar(Car):
# 	"""电动车的独特之处"""
# 	def __init__(self, make, model, year):
# 		super().__init__(make, model, year)
		

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())



#将实例用作属性
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
		
	def increment_odometer(self,miles):
		self.odometer_reading += miles

class Battery():
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + "-KWh battery!")

	def get_range(self):
		"""打印一条消息，显示电池续航里程"""
		if self.battery_size == 70:
			range = 200
		elif self.battery_size == 85:
			range =275

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def up_battery_rang(self,upbattery):
		self.battery_size = upbattery

class ElectricCar(Car):
	"""电动车的独特之处"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	# def describe_battery(self):
	# 	print("This car has a " + str(self.battery_size) + "-KWh battery!")

	def fill_gas_tank():
		print('This car does not need a gas tank!')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.up_battery_rang(85)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



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
		user_info = self.first_name + " " + self.last_name + "," + ta + " is "
		user_info += str(self.age) + " is " + self.sex + "."
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

class Privileges():
	"""docstring for privileges"""
	def __init__(self, privileges_list=['can add post','can delete post','can ban user']):
		self.privileges_list = privileges_list

	def show_privileges(self):
		for privilege in self.privileges_list:
			print("Admin have " + privilege)

class Admin(User):
	"""docstring for Adimn"""
	def __init__(self, first_name, last_name, age, sex):
		super().__init__(first_name, last_name, age, sex)
		self.privileges = Privileges()

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

admin_user = Admin('li','hua',14,'man')
admin_user.privileges.show_privileges()
print(admin_user.describe_user())