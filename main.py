from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score



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

# score
score = Score()


# listen for key press
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")


screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()