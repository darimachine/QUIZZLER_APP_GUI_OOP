from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.score =0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canva = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canva.create_text(150,125,text="aaaaaa",font=("Arial",20,"italic"),width=280)
        self.canva.grid(row=1,column=0,columnspan=2,pady=50,padx=50)
        #right wrong buttons
        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")
        self.right_btn = Button(image=right,highlightthickness=0,command=self.right_answer)
        self.wrong_btn = Button(image=wrong,highlightthickness=0,command=self.wrong_answer)
        self.right_btn.grid(row=2,column=0)
        self.wrong_btn.grid(row=2,column=1)
        #label
        self.score_lbl = Label(text=f"Score: {self.score}",bg=THEME_COLOR,fg="white",font=(10))
        self.score_lbl.grid(row=0,column=1)

        self.get_next_question()
        self.window.mainloop()
    def right_answer(self):
        if self.quiz.check_answer("True"):
            self.score += 1
            self.score_lbl.config(text=f"Score: {self.score}")
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.is_right = self.window.after(1000, self.get_next_question)
    def wrong_answer(self):

        if self.quiz.check_answer("False"):
            self.score += 1
            self.score_lbl.config(text=f"Score: {self.score}")
            self.canva.config(bg="green")

        else:
            self.canva.config(bg="red")
        self.is_right = self.window.after(1000, self.get_next_question)
    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text,text=q_text)
        else:
            self.canva.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")





