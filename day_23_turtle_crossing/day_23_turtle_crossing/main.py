import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
while game_is_on:
    if len(car_manager.cars) < 20:
        car_manager.create_cars()
    time.sleep(0.05)
    screen.update()
    if player.detect_win():
        player.reset_player()
        scoreboard.level_complete()
    car_manager.move(scoreboard.level)

    for car in car_manager.cars:
        if -10 <= car.xcor() <= 10:
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
