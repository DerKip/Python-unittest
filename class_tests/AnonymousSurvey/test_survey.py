
import unittest
from survey import AnonymousSurvey
 
class SurveyTestCase(unittest.TestCase):
    """Testing AnonymousSurvey class"""


    def setUp(self):
        """
        create a survey and a set of responses for use in all test methods
        """
        question="What is your favourite text editor? "
        self.my_survey=AnonymousSurvey(question)
        self.responses=['sublime','Brackets','Pycharm']

    def test_store_single_response(self):
        """Tests that a single response is stored properly"""
        self.my_survey.store_response("VSCode")
        self.assertIn("VSCode",self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Tests that three responses are stored properly"""
        
        for response in self.responses:
            self.my_survey.store_response(response)
            self.assertIn(response,self.my_survey.responses)

unittest.main()