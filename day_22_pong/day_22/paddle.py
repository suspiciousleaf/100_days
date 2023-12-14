from turtle import Turtle

STARTING_POSITION = ()
MOVE_DISTANCE = 40
PADDLE_HORIZONTAL_OFFSET = 350
PADDLE_WIDTH = 5


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.speed("fastest")
        self.setpos(self.paddle_offset, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(PADDLE_WIDTH, stretch_len=1)

    def up(self):
        y_cor = self.ycor()
        if y_cor <= 230:
            self.goto(self.paddle_offset, y_cor + MOVE_DISTANCE)

    def down(self):
        y_cor = self.ycor()
        if y_cor >= -230:
            self.goto(self.paddle_offset, y_cor - MOVE_DISTANCE)


class PaddleRight(Paddle):
    def __init__(self):
        self.paddle_offset = PADDLE_HORIZONTAL_OFFSET
        super().__init__()


class PaddleLeft(Paddle):
    def __init__(self):
        self.paddle_offset = -PADDLE_HORIZONTAL_OFFSET
        super().__init__()
