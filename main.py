from data import questions_data
from questionmodel import Questions
from quizbrain import QuizBrain
from userinterface import QuizInterface

question_bank = []
total_questions = 0

for item in questions_data:
	question_object = Questions(item['question'], item['correct_answer'])
	question_bank.append(question_object)
	total_questions += 1


quiz = QuizBrain(question_bank)
display = QuizInterface(quiz, total_questions)