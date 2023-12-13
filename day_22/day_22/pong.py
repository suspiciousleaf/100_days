# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_22/day_22_env/Scripts/Activate.ps1

from turtle import Screen
import time
from paddle import PaddleRight, PaddleLeft
from ball import Ball
from scoreboard import Scoreboard

UPDATE_INTERVAL = 0.025

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

game_is_on = True
paddle_right = PaddleRight()
paddle_left = PaddleLeft()
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")

screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

while game_is_on:
    time.sleep(UPDATE_INTERVAL)
    screen.update()
    ball.move()

    for paddle in paddle_left, paddle_right:
        ball.detect_paddle(paddle)

    if ball.xcor() > 380:
        scoreboard.increase_score_left()
        ball.ball_reset()
    elif ball.xcor() < -380:
        scoreboard.increase_score_right()
        ball.ball_reset()

    if scoreboard.current_score_left + scoreboard.current_score_right == 7:
        ball.hideturtle()
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
