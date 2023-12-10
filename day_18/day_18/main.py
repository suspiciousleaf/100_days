import turtle as t
import random

import colorgram


rgb_colours = []
colours = colorgram.extract("day_18/day_18/hirst.jpg", 30)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    # Remove almost white colours sourced from background
    if r + g + b < 725:
        rgb_colours.append((r, g, b))

# 10 * 10 spots
# each dot 20 pixels, spaced 50 pixels

tim = t.Turtle()
tim.shape("turtle")
tim.color("black")
tim.fillcolor("SeaGreen")
tim.up()

t.colormode(255)
tim.speed(0)
tim.hideturtle()

for x in range(-250, 250, 50):
    for y in range(-250, 250, 50):
        tim.setpos(x, y)
        tim.dot(20, random.choice(rgb_colours))


screen = t.Screen()
screen.exitonclick()
