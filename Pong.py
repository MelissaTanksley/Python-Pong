# Simple Pong in Python 3
# By Joe Panetta

import turtle
import winsound

win = turtle.Screen()
win.title("Joe's Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score starting at zero
score_1 = 0
score_2 = 0

# Player1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

# Player_2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# pen.write("EPIC PONG 2020!!", align="", font=("Courier", 24, "normal"))
pen.write("Player 1: 0 Payer 2: 0", align="center", font=("Courier", 18, "normal"))



# Functions to move paddles
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)


def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# keyboard controlls

win.listen()
win.onkeypress(player_1_up, "w")
win.onkeypress(player_1_down, "s")
win.onkeypress(player_2_up, "Up")
win.onkeypress(player_2_down, "Down")

# Main game loop
while True:
    win.update()
    
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # When the ball hits a border

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.Beep(37, 3)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Beep(37, 3)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Payer 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Payer 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    # When the ball hits a players paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.Beep(6000, 200)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.Beep(4000, 200)

