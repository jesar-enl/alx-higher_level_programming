#!/usr/bin/python3
"""Module containing the Survey class"""


class AnnonymousSurvey(object):
    """Collect annonymous answers toa survey question."""
    def __init__(self, question):
        """Store a question, prepare to store responses
        Args:
            question: the question to be asked.
            responses: a list of expected answers from users
        """
        super(AnnonymousSurvey, self).__init__()
        self.question = question
        self.responses = []

    def show_question(self):
        """The question for the poll."""
        print(self.question)

    def store_response(self, new_response):
        """Stor a single response to the survey.

        Args:
            new_response: answer from the user
        """
        self.responses.append(new_response)

    def show_results(self):
        """shaow all the results from the poll."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
