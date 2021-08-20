from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-25, 0), (-50, 0)]
MOVE_DISTANCE = 10
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            self.create_part(coordinates)

    def create_part(self, position):
        snake_part = Turtle('square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.goto(position)
        self.parts.append(snake_part)

    def extend(self):
        self.create_part(self.parts[-1].position())

    def move(self):
        for snake_part in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[snake_part - 1].xcor()
            new_y = self.parts[snake_part - 1].ycor()
            self.parts[snake_part].goto(new_x, new_y)
        self.parts[0].forward(MOVE_DISTANCE)

    def reset(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]

    def move_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def move_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def move_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def move_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)