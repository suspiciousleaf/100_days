# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_19/day_19_env/Scripts/Activate.ps1

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("black")
tim.fillcolor("SeaGreen")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.penup()
    tim.clear()
    tim.setpos(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
