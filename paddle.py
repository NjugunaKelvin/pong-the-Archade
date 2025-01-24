from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
    
    def right_paddle(self):
        self.goto(350, 0)
    
    def left_paddle(self):
        self.goto(-350, 0)

    # go_up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # go_down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)