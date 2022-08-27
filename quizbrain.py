import html

class QuizBrain:
    def __init__(self, parm_question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = parm_question_list

    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     new_question = html.unescape(current_question.text)
    #     print(new_question)
    #     print(current_question.answer)

    def check_answer(self, user_answer):
        current_question = self.question_list[self.question_number]
        if user_answer == current_question.answer:
            self.score += 1
            return True
        else:
            return False
