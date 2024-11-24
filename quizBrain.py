class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self._question_list=q_list
    def still_has_question(self):
        return self.question_number< len(self._question_list)
    def next_question(self):
        currect_question= self._question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"q.{self.question_number}:{currect_question.text}Ttrue/False:")
        self.cheak_answer(user_answer,currect_question.answer)

    def cheak_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got in rigght")
        else:
            print("That's wrong")
        print(f"the correct answer was {correct_answer}.")
        print(f"Your currect score is {self.score}/{self.question_number}")
        print("\n")