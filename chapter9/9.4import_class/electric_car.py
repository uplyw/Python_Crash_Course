from car import Car

class Battery():
	"""docstring for Battery"""
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-KWh battery!")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 280
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

class ElectricCar(Car):
	"""docstring for ClassName"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
		