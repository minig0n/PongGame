from turtle import Turtle
from main_configurations import *


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < SCREEN_HEIGHT/2 - 60:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > - SCREEN_HEIGHT / 2 + 70:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
