import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('li', 'lei')
		self.assertEqual(formatted_name, 'Li Lei')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('han', 'mei', 'mei')
		self.assertEqual(formatted_name,'Han Mei Mei')
unittest.main()