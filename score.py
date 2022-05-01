from turtle import Turtle


class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(150, -300)
        self.write(f"Your score: {score}/50", font=("cambria",20))

