from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple", "black"]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 5
NEW_CAR_CHANCE = 0.15


class CarManager:
    def __init__(self) -> None:
        self.cars = []

    def create_cars(self):
        if random.random() > 1 - NEW_CAR_CHANCE:
            new_car = Turtle()
            new_car.move_speed = random.randint(3, 7)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.setpos(310, random.choice(range(-220, 221, 20)))
            self.cars.append(new_car)

    def move(self, level):
        for car in self.cars:
            car.forward((1 + (0.25 * level)) * car.move_speed)
            if car.xcor() < -310:
                car.setpos(310, random.choice(range(-220, 221, 20)))
