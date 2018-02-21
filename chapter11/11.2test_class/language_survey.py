# language_survey
from survey import AnonymousSurvey

question = "what language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("enter 'q' to quit" )
while True:
	response = input("language:")
	if response == 'q':
		break

	my_survey.store_response(response)

print('\nThank you to everyone did you first learn to speak')
my_survey.show_results()