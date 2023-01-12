#!/usr/bin/python3
"""Module containing the tests for the Annonymous Survey class"""

import unittest
from survey import AnnonymousSurvey


class TestAnnonymousSurvey(unittest.TestCase):
    """Test for class AnnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set
        of responses for use in all test
        methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', 'Luganda', 'Lusoga']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        # super(TestAnnonymousSurvey, self).__init__()
        # question = "What language did you first learn to speak?"
        # my_survey = AnnonymousSurvey(question)
        # access the responses in the list
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses ares stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Luganda']
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
