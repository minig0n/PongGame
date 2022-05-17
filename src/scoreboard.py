from turtle import Turtle
from main_configurations import *


class BackGround(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, int(SCREEN_HEIGHT / 2))
        self.middle_line()

    def middle_line(self):
        self.pendown()
        self.setheading(270)
        for trace in range(0, int(SCREEN_HEIGHT/20)):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME  OVER", align=ALIGNMENT, font=FONT)


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score_player = -1
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.position = position
        self.add_score()

    def add_score(self):
        self.score_player += 1
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score_player}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
