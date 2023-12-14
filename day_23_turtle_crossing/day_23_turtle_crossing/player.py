from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_player()
        self.finish_line = FINISH_LINE_Y

    def reset_player(self):
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.speed("fastest")
        self.color("black")
        self.fillcolor("green")
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() >= -270:
            self.backward(MOVE_DISTANCE)

    def detect_win(self):
        return self.ycor() >= FINISH_LINE_Y
