from turtle import Turtle,Screen
screen=Screen()

class Paddler(Turtle):
    def __init__(self,positioin):
        super().__init__()
        self.shape("square")

        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")

        self.goto(positioin)





    def go_up(self):
        new_y=self.ycor()+30
        self.goto(self.xcor(),new_y)
        # if seg_list
        # self.seg_list[0].forward(20)
        #

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

