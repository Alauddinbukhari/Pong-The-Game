from turtle import Turtle,Screen
screen=Screen()
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(0,0)
        self.movement_sp=0.1
        self.y_move=10
        self.x_move=10



    def move_random(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move


        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
    def reset_position(self):
        self.goto(0,0)
        self.movement_sp=0.1
        self.bounce_x()
    def increase_speed(self):
        self.movement_sp*=0.9


