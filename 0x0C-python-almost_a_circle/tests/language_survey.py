#!/usr/bin/python3
"""Module to contain the survey for language"""


from survey import AnnonymousSurvey


# Define  a question, make a survey.
question = "What language did you first learn to speak?"
my_survey = AnnonymousSurvey(question)

# Show the question, and store the responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
