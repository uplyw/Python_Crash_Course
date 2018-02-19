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
		print('This car has a ' + str(self.battery_size) + "-KWh battary!")

class ElectricCar(Car):
	"""电动车的独特之处"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	# def describe_battery(self):
	# 	print("This car has a " + str(self.battery_size) + "-KWh battary!")

	def fill_gas_tank():
		print('This car does not need a gas tank!')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()