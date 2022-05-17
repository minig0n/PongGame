from turtle import Turtle
from main_configurations import *
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.direction = 0
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=BALL_SIZE, stretch_wid=BALL_SIZE)
        self.penup()
        self.vel_ball = BALL_VELOCITY

    def move(self):
        self.forward(self.vel_ball)

    def initialize_left(self):
        self.vel_ball = BALL_VELOCITY
        random_position = random.randint(0, 1)
        self.goto(BALL_START[random_position])
        if random_position == 0:
            self.direction = random.randint(180 + MINIMUM_ANGLE, 180 + MAXIMUM_ANGLE)
        else:
            self.direction = random.randint(180 - MAXIMUM_ANGLE, 180 - MINIMUM_ANGLE)
        self.setheading(self.direction)

    def initialize_right(self):
        self.vel_ball = BALL_VELOCITY
        random_position = random.randint(0, 1)
        self.goto(BALL_START[random_position])
        if random_position == 0:
            self.direction = random.randint(360 - MAXIMUM_ANGLE, 360 - MINIMUM_ANGLE)
        else:
            self.direction = random.randint(MINIMUM_ANGLE, MAXIMUM_ANGLE)
        self.setheading(self.direction)

    def paddle_bounce(self):
        angle_increment = random.randint(- ANG_INCREMENT, ANG_INCREMENT)
        self.direction = 180 - self.direction + angle_increment
        self.setheading(self.direction)

    def wall_bounce(self):
        velocity_increment = random.randint(0, VEL_INCREMENT)
        self.direction = - self.direction
        self.vel_ball += velocity_increment
        self.setheading(self.direction)

    def right_debug(self):
        self.goto(self.xcor() - 10, self.ycor())

    def left_debug(self):
        self.goto(self.xcor() + 10, self.ycor())
