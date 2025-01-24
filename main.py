from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game") 

# remove the animation
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

# go_up
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

# go_down
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

# listen for key press
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()