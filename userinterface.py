from tkinter import *
from quizbrain import QuizBrain
import html

class QuizInterface:
    def __init__(self, quizbrain:QuizBrain, num_of_qns):
        self.quiz = quizbrain
        self.totalquestions = num_of_qns
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.configure(padx=20, pady=20, bg='grey')
        self.score_text = f"Score: {self.quiz.score}"
        self.scorelabel = Label(text=self.score_text, padx=10, pady=10, bg='grey', font='Arial 15 bold')
        self.scorelabel.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.configure(bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='This is the question text', font='Arial 20 italic', fill='black', width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1, pady=20)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg='white')
        current_question = self.quiz.question_list[self.quiz.question_number]
        q_text = html.unescape(current_question.text)
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.quiz.question_number += 1

    def true_clicked(self):
        res = self.quiz.check_answer('True')
        self.give_feedback(res)

    def false_clicked(self):
        res = self.quiz.check_answer('False')
        self.give_feedback(res)

    def give_feedback(self, feedbk):
        if self.quiz.question_number < self.totalquestions-1:
            self.score_text = f"Score: {self.quiz.score}"
            self.scorelabel.config(text=self.score_text)

            if feedbk:
                self.canvas.config(bg='green')
            else:
                self.canvas.config(bg='red')
            self.window.after(500, self.next_question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Game Over! Your score is {self.quiz.score}/{self.totalquestions}")
