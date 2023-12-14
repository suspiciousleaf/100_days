from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):  # Make sure food doesn't appear inside snake
        random_coords = (
            random.choice(range(-280, 280, 20)),
            random.choice(range(-280, 280, 20)),
        )

        self.goto(random_coords)
