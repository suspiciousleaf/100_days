from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Pick a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for i, colour in enumerate(colours):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color("black")
    turtle.fillcolor(colour)
    turtle.setpos(x=-230, y=(-125+(i*50)))
    turtles.append(turtle)


def move_forward(turtle):
    turtle.forward(random.randint(5, 15))


if user_bet:
    not_finished = True

while not_finished:
    turtle_positions = []
    for turtle in turtles:
        move_forward(turtle)
        turtle_positions.append(turtle.pos()[0])

    max_pos = max(turtle_positions)
    if max_pos >= 200:
        not_finished = False


for turtle in turtles:
    if turtle.pos()[0] == max_pos:
        colour = turtle.color()[1]
        if colour == user_bet:
            print("You win!")
        else:
            print(f"You lose, the winning turtle was {colour}.")

screen.exitonclick()
