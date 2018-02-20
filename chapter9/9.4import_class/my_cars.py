# from car import Car,ElectricCar
from car import Car
from electric_car import ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2016)
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'model s', 2018)
my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())