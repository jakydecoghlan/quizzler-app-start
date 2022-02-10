from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text="{QuizBrain.q_text}")
        self.canvas.grid(column=0, row=1, columnspan=2)

        # self.question = Label()
        # self.question.grid(column=0, row= 1, columnspan=2)

        self.score = Label(text="score = {QuizBrain.score}", fg="white")
        self.score.config(padx=50, pady=50, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(text="Button", image=self.true_image)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(text="Button", image=self.false_image)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
