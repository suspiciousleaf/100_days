from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level:2}", align="center", font=FONT)

    def level_complete(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align="center", font=("courier", 36, "bold"))
