class QuizBrain:
    def __init__(self, question_list: list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q. {self.question_number}: {self.question.text} (True/False): "
        )
        self.check_answer(user_answer, self.question.answer)
