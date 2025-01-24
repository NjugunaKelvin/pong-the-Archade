from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.color("blue")
        self.penup()
        
    
    def move(self):
        xcor = self.xcor() + 10
        ycor = self.ycor() + 10
        self.goto(xcor, ycor)