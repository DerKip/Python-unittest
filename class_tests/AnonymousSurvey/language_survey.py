
from survey import AnonymousSurvey

#Define a question and make a survey
question="What is your favourite programming language? "
my_survey=AnonymousSurvey(question)

#Show the question and show the responses to the question
print(my_survey.show_questions())
print("To quit enter q ")
while True:
    inp=input("Enter your response:")
    if inp=='q':
        break
    my_survey.store_response(inp)

#Show the survey results
print("\n Thank you for your for your response in the survey \n Here are the results")
my_survey.show_results()
# total=dict(my_survey.responses)
# for a,b in total.items():
#     if b==1:
#         print("-"+a)
#     print('-'+a,b)
