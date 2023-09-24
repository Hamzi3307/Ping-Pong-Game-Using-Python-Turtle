from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

my_scr = Screen()
my_scr.setup(height=600, width= 800)
my_scr.bgcolor("black")
my_scr.title("PONG")
my_scr.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

my_scr.listen()
my_scr.onkey(r_paddle.up, "Up")
my_scr.onkey(r_paddle.down, "Down")
my_scr.onkey(l_paddle.up, "w")
my_scr.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.velocity)
    ball.move()
    my_scr.update()
    
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    #Detect Collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.x_bounce()
        
    #Detect when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    
    #Detect when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()   


my_scr.exitonclick()