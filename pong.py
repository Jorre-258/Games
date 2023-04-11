import turtle

#making the screen

wn = turtle.Screen()
wn.title("Made By Jorre")
wn.bgcolor("black")
wn.setup(width=800, height=550)
wn.tracer(0)

# make left paddle

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.turtlesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#make right paddle

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.turtlesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

#make the ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#def paddle movement

def paddle_A_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_A_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_B_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_B_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_A_up, "z")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "o")
wn.onkeypress(paddle_B_down, "l")

#game loop

while True:
    wn.update()

    # make the ball move

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    if ball.ycor() > 265:
        ball.sety(265)
        ball.dy *=-1

    if ball.ycor() < -265:
        ball.sety(-265)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx*= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx*= -1

    # make the paddle bounce

    if ball.xcor() > 340 and ball.xcor() < 350and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
       ball.setx(340)
       ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
       ball.setx(-340)
       ball.dx *= -1


