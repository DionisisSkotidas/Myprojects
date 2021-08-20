import turtle
import random
from turtle import Turtle, Screen


def random_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def next_line(who, line):
    who.setpos(x=0.00, y=line * 15)
    who.left(90)
    who.forward(15)
    who.pencolor(random_rgb_color())
    who.dot(size=10)
    who.right(90)


def vertical_line(who, dots):
    for dot in range(dots):
        who.pencolor(random_rgb_color())
        who.dot(size=10)
        who.forward(15)


if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    x_position = 505
    y_position = 450
    xelonas = Turtle()
    xelonas.color('red')
    xelonas.shape('turtle')
    # xelonas.up()
    xelonas.speed('fastest')

    for i in range(180):
        xelonas.pencolor(random_rgb_color())
        xelonas.circle(100)
        xelonas.right(3)

    screen.exitonclick()
