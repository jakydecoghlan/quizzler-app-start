from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

import time


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="{QuizBrain.q_text}",
                                                     fill=THEME_COLOR,
                                                     font="arial 20 italic")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)



        # self.question = Label()
        # self.question.grid(column=0, row= 1, columnspan=2)

        self.score = Label(text="Score = 0", anchor='center', font="arial 10 bold", fg="white")
        self.score.config(bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.score.config(padx=20, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(text="Button", image=true_image, bg=THEME_COLOR, highlightthickness=0,
                                  command=self.true_answer
                                  )
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(text="Button", image=false_image, bg=THEME_COLOR, highlightthickness=0,
                                   command=self.false_answer
                                   )
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_answer(self):
        is_right = (self.quiz.check_answer("false"))
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
            # self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
            #


