from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score = 0
        self.setpos(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.current_score:2}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=GAME_OVER_FONT,
        )
