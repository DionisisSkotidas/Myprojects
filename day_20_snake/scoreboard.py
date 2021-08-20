from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.show_score()

    def update_scoreboard(self):
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f'Score: {self.score}\t High Score : {self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()



