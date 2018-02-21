import unittest
from city_functions import city_country_fun
class city_country_test(unittest.TestCase):
	"""docstring for ClassName"""
	def test_city_country(self):
		city_country_name = city_country_fun('beijing', 'china')
		self.assertEqual(city_country_name, 'beijing in china')
unittest.main()