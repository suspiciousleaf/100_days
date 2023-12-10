# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_18/day_18_env/Scripts/Activate.ps1

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("black")
tim.fillcolor("SeaGreen")

t.colormode(255)
tim.speed(0)


def random_colour():
    return tuple(random.choice(range(256)) for _ in range(3))


#! Concentric shapes challenge
# for x in range(3, 11):
#     tim.pencolor(random_colour())
#     for _ in range(x):
#         tim.forward(100)
#         tim.right(360 / x)

#! Random walk
# headings = [0, 90, 180, 270]

# tim.pensize(10)
# for _ in range(500):
#     tim.pencolor(random_colour())
#     tim.setheading(random.choice(headings))
#     tim.fd(20)

iterations = 60
for _ in range(iterations):
    tim.pencolor(random_colour())
    tim.circle(100)
    tim.right(360 / iterations)

screen = t.Screen()
screen.exitonclick()
