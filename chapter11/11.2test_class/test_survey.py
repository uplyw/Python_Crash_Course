import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""docstring for ClassName"""
	def test_store_single_response(self):
		question = "what language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		
		self.assertIn('English', my_survey.responses)

	def test_store_three_response(self):
		question = "what language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English','java','python']
		for response in responses:
			my_survey.store_response(response)
		for response in responses:
			self.assertIn(response, my_survey.responses)
		# self.assertIn('English', my_survey.responses)
unittest.main()