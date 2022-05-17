from turtle import Screen, Turtle
from main_configurations import *
from scoreboard import BackGround, ScoreBoard
from players import Player
from ball import Ball
import time


screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

background = BackGround()
score1 = ScoreBoard((-50, SCREEN_HEIGHT / 2 - 70))
score2 = ScoreBoard((50, SCREEN_HEIGHT / 2 - 70))
player1 = Player((-SCREEN_WIDTH/2 + 30, 0))
player2 = Player((SCREEN_WIDTH/2 - 30, 0))
ball = Ball()

screen.listen()
screen.onkey(player1.go_up, "w")
screen.onkey(player1.go_down, "s")
screen.onkey(player2.go_up, "Up")
screen.onkey(player2.go_down, "Down")

pause_screen = Turtle()
pause_screen.hideturtle()


def pause():
    global paused
    if not paused:
        pause_screen.color("white")
        pause_screen.write("Pause", align=ALIGNMENT, font=FONT)
        paused = True
    else:
        pause_screen.clear()
        paused = False


screen.onkey(pause, "space")

ball.initialize_left()

paused = False
game_is_on = True
while game_is_on:
    if not paused:
        screen.update()
        time.sleep(1/VELOCITY)
        ball.move()

        # 10 points end game
        if score1.score_player == 5 or score2.score_player == 5:
            game_is_on = False
            background.game_over()

        # Detect left goal
        if ball.xcor() > int(SCREEN_WIDTH/2) + 250:
            score1.add_score()
            ball.initialize_right()

        # Detect right goal
        if ball.xcor() < -int(SCREEN_WIDTH / 2) - 250:
            score2.add_score()
            ball.initialize_left()

        # Paddle collision
        if ball.xcor() < -SCREEN_WIDTH/2 + 50 and ball.distance(player1) < 60:
            ball.left_debug()
            ball.paddle_bounce()

        if ball.xcor() > SCREEN_WIDTH/2 - 50 and ball.distance(player2) < 60:
            ball.right_debug()
            ball.paddle_bounce()

        # Wall collision
        if ball.ycor() > int(SCREEN_HEIGHT/2) - 20 or ball.ycor() < -int(SCREEN_HEIGHT/2) + 20:
            ball.wall_bounce()
    else:
        screen.update()

screen.exitonclick()
