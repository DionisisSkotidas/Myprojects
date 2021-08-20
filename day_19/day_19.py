from turtle import Turtle, Screen
import random

def forward():
    xelwnas.forward(30)


def backwards():
    xelwnas.backward(30)


def turn_left():
    xelwnas.left(10)


def turn_right():
    xelwnas.right(10)


def clear():
    xelwnas.clear()
    xelwnas.penup()
    xelwnas.home()
    xelwnas.pendown()


def take_users_guess():
    user_guess = screen.textinput(title='kalhspera', prompt='diale3e xrwma bro')
    if user_guess in color_list:
        return user_guess
    else:
        print("Sorry we don't have that color today \n"
              "Please try again")
        take_users_guess()


screen = Screen()
color_list = ["red", "orange", "yellow", "blue", "green", "purple"]


width, height = 500, 500
screen.setup(width, height)
user_bet = take_users_guess()
game_on = False

xelonitzakia = []
x, y = -240, -130
for i in range(6):
    xelwnas = Turtle(shape='turtle')
    xelwnas.color(color_list[i])
    xelwnas.penup()
    xelwnas.goto(x, y)
    y += 50
    xelonitzakia.append(xelwnas)

if user_bet:
    game_on = True

while game_on:
    random_speed = random.randint(0, 10)
    random_turtle = random.choice(xelonitzakia)
    random_turtle.forward(random_speed)

    if random_turtle.xcor() > 230:
        winning_color = random_turtle.pencolor()
        if winning_color == user_bet:
            print(f"Congratulations you won.The winning turtle was {winning_color}")
        else:
            print(f"Sorry mate you lost.The winning turtle turned out to be {winning_color}")
        game_on = False


print('end')

screen.exitonclick()