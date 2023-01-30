from turtle import Turtle
#usng my logic and angela logic is different

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,230)
        self.l_score = 0
        self.r_score = 0
        self.write(arg=f"ScoreBoard\n {self.l_score}   |    {self.r_score}",align="Center",font=("gooddog",25,'normal'))
    def current_score(self):

        self.write(arg=f"ScoreBoard\n {self.l_score}   |    {self.r_score}",align="Center",font=("gooddog",25,'normal'))
    def update_lscore(self):
        self.clear()
        self.l_score+=1
        self.current_score()

    def update_rscore(self):
        self.clear()
        self.r_score+=1
        self.current_score()


