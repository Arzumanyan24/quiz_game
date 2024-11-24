# from data import question_data

# class Quession:
#     def __init__(self,score,question):
#         self.score=score
#         self.question=question
       


#     def sistem(self):
#         for i in question_data:
#             print(i["question"])
#             answer=input("true or False")
#             if answer == i["correct_answer"]:
#                 self.score += 1
#                 self.question += 1
#                 print(f"{self.score}/{self.question}")
#             else:
#                 print(i["correct_answer"])
#                 self.question+=1
#                 print(f"{self.score}/{self.question}")
# game=Quession(0,0)
# print(game.sistem())




from questionmodel import Question
from data import question_data
from quizBrain import QuizBrain
question_bank=[]
for question in question_data:
    question_text= question["question"]
    question_answer=question["correct_answer"]
    new_question= Question(question_text,question_answer)
    question_bank.append(new_question)

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")


    