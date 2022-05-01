from turtle import Turtle

class Label(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.state = state
        self.x = x
        self.y = y
        self.hideturtle()
        self.move()
        self.write(state)

    def move(self):
        self.penup()
        self.goto(self.x, self.y)
