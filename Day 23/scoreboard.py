from turtle import Turtle

FONT1 = ("Courier", 16, "normal")
FONT2 = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.score = 0
        self.goto(-250, 250)
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT2)

    def update_score(self):
        self.score +=1
        self.level +=1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT2)