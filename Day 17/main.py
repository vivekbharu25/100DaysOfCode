from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data[0]["results"]:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    comp_quest = Question(question_text, question_ans)
    question_bank.append(comp_quest)

quiz = QuizBrain(question_bank)
game_on = True
while quiz.still_has_questions() and game_on:
    quiz.next_question()
