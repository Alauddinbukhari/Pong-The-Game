
def game():
    from scoreboard import Scoreboard
    from turtle import Turtle,Screen
    import time
    from padle import Paddler
    from ball import ball
    scoreboard=Scoreboard()
    screen=Screen()
    screen.setup(height=600,width=800)#x=400,y=300
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    ball=ball()
    l_paddle=Paddler(positioin=(-350, 0))
    r_paddle=Paddler(positioin=(350, 0))

    screen.onkey(l_paddle.go_up,key= "w")
    screen.onkey(l_paddle.go_down, key="s")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")


    Gameison= True

    while Gameison:

        screen.update()
        time.sleep(ball.movement_sp)
        ball.move_random()
        #Detect with the collision with wall
        if ball.ycor()>280 or ball.ycor()<-280:
            ball.bounce_y()
        #detect the paddle and bounce back
        if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
            ball.bounce_x()
            ball.increase_speed()
        if ball.xcor()>400:
            scoreboard.update_lscore()
            ball.reset_position()

        if ball.xcor()<-400:
            scoreboard.update_rscore()
            ball.reset_position()


        # if r_paddle.distance(ball)<30 or l_paddle.distance(ball)<30:
        #     ball.xcor()
        #     ball.ycor()
        #     ball.bounce_back()
    screen.listen()


    screen.exitonclick()



game()