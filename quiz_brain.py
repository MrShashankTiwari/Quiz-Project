class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.total = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q{self.question_number }. {current_question.text} (True/False): ").title()
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            self.total += 1
            print(
                f"You got it right! \nThe correct answer was: {correct_answer}.")
            print(f"Your current score is {self.score}/{self.total}")
        else:
            self.total += 1
            print(f"That's wrong :( \nThe correct answer is {correct_answer}.")
            print(f"Your current score is {self.score}/{self.total}")
