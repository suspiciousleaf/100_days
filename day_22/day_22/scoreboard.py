from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score_left = 0
        self.current_score_right = 0
        self.setpos(0, 200)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.current_score_left}          {self.current_score_right}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score_left(self):
        self.current_score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.current_score_right += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        if self.current_score_left > self.current_score_right:
            winner = "Left"
        else:
            winner = "Right"
        self.write(
            f"GAME OVER\n{winner} wins!",
            align=ALIGNMENT,
            font=GAME_OVER_FONT,
        )
