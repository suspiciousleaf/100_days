# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_20/day_20_env/Scripts/Activate.ps1

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

UPDATE_INTERVAL = 0.1

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(UPDATE_INTERVAL)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if not (-290 <= snake.head.xcor() <= 290 and -290 <= snake.head.ycor() <= 290):
        # game_is_on = False
        score.reset_game()
        snake.reset_snake()

    # Detect collisions with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset_game()
            snake.reset_snake()


screen.exitonclick()
