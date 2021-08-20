from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BORDER = 300

#               SET UP
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(snake.move_north, 'Up')
screen.onkeypress(snake.move_west, 'Left')
screen.onkeypress(snake.move_east, 'Right')
screen.onkeypress(snake.move_south, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.make_food()
        snake.extend()

#     HIT  THE BORDERS
    if snake.head.xcor() > BORDER or snake.head.xcor() < -BORDER or snake.head.ycor() > BORDER or snake.head.ycor() < -BORDER:
        scoreboard.reset()
        snake.reset()

    for part in snake.parts:
        if part == snake.head:
            pass
        elif part.distance(snake.head) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()