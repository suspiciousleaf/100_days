# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_17/day_17_env/Scripts/Activate.ps1
import html
from data import question_data

from question_model import Question
from quiz_brain import QuizBrain

question_bank = [
    Question(html.unescape(line["question"]), line["correct_answer"])
    for line in question_data
]

quiz = QuizBrain(question_bank)

print("\n")
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Final score: {quiz.score}/{quiz.question_number}\n")
