from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.color("White")
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score +=1
        self.clear()
        self.update()
