from turtle import Turtle
import random
import time

SIZE_FACTOR = 1
SHAPE = "circle"
COLOUR = "white"
STEP = 5


class Ball(Turtle):
    # Dict to hold the movement directions. 0: down left, 1: up left, 2: down right, 3: up right
    dir_dict = {0: (-STEP, -STEP), 1: (-STEP, STEP), 2: (STEP, -STEP), 3: (STEP, STEP)}

    def __init__(self) -> None:
        super().__init__()
        self.direction = random.randint(0, 3)
        self.create_ball()

    def create_ball(self):
        self.penup()
        self.speed("fastest")
        y_cor_random = random.choice(range(-240, 260, 20))
        self.setpos(0, y_cor_random)
        self.color(COLOUR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=SIZE_FACTOR, stretch_len=SIZE_FACTOR)

    def ball_reset(self):
        self.clear()
        time.sleep(1)
        self.direction = random.randint(0, 3)
        self.create_ball()

    def move(self):
        x_cor_new = self.xcor() + self.dir_dict[self.direction][0]
        y_cor_new = self.ycor() + self.dir_dict[self.direction][1]
        self.goto(x_cor_new, y_cor_new)

        if self.ycor() < -260 or self.ycor() > 260:
            self.edge_bounce()

    def edge_bounce(self):
        if self.ycor() > 260:
            self.direction -= 1
        elif self.ycor() < -260:
            self.direction += 1

    def paddle_bounce(self):
        if self.direction in (0, 1):
            self.direction += 2
        elif self.direction in (2, 3):
            self.direction -= 2

    def detect_paddle(self, paddle):
        if not -330 <= self.xcor() <= 330 and self.distance(paddle) < 50:
            self.paddle_bounce()
