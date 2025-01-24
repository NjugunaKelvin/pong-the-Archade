from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game") 

# remove the animation
screen.tracer(0)

right_paddle = Paddle()
right_paddle.right_paddle()

left_paddle = Paddle()
left_paddle.left_paddle()

# ball
ball = Ball()



# listen for key press
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")


screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()