class QuizBrain:
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num +=1
        self.u_inp = input(f"Q-{self.question_num}: {current_question.question}(True/False):").lower()
        if self.u_inp == "true" or self.u_inp == "t":
            self.u_inp = "True"
        elif self.u_inp == "false" or self.u_inp == "f":
            self.u_inp = "False"
        else:
            self.u_inp = ""
        self.check_answer(current_question.reply, self.u_inp)
        if self.question_num == len(self.question_list):
            print(f"You've completed the quiz \nYour Final Score is {self.score}/{self.question_num}")

    def check_answer(self, correct_answer, user_answer ):
        if user_answer == correct_answer:
            self.score+=1
            print("Hurray...It's right.")
        else:
            print("Oh,ho...That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_num}")
        print("\n")