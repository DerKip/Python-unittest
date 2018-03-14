
class AnonymousSurvey():
    """Collects anonymous answers to a survey question"""

    def __init__(self,question):
        """Store a question and prepare to store response"""
        self.question=question
        self.responses=[]

    def show_questions(self):
        """Shows the questions"""
        return self.question
    
    def store_response(self,new_response):
        """Stores a response to the survey """
        self.responses.append(new_response)

    def show_results(self):
        """Shows the results of the anonymous survey"""
        for response in self.responses:
            print ('-'+response)
  