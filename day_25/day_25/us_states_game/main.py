import turtle
import pandas as pd

FONT_STATES = ("Courier", 12, "bold")
FONT_SCORE = "Courier", 24, "bold"

screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.tracer(0)

image = "day_25//day_25//us_states_game//blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pd.read_csv("day_25//day_25//us_states_game//50_states.csv")

all_states = data["state"].to_list()

game_running = True

state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.setpos(0, 200)

score = 0

correct_guesses = []


def update_score():
    score_writer.clear()
    score_writer.write(f"{score} / 50", align="center", font=FONT_SCORE)


def find_and_print_state(answer_state):
    state_entry = data[data["state"] == answer_state]
    state_writer.setpos(state_entry.x.iloc[0], state_entry.y.iloc[0])
    state_writer.write(answer_state, align="center", font=FONT_STATES)


game_running = True

screen.update()
while game_running:
    answer_state = screen.textinput(
        title="Guess the State", prompt="Enter the name of a U.S. state"
    ).title()

    if answer_state == "Exit":
        game_running = False
        state_writer.color("red")
        for state in all_states:
            if state not in correct_guesses:
                find_and_print_state(state)

    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        find_and_print_state(answer_state)
        score += 1
        update_score()
    screen.update()

    if len(correct_guesses) == 50:
        game_running = False

screen.mainloop()
