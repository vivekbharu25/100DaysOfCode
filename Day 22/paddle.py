from turtle import Turtle

UPPER_LIMIT = 210
LOWER_LIMIT = -210

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(pos)

    # def move(self):
    #     self.paddle.setheading()
    #     self.paddle.forward(MOVE_DISTANCE)

    def up(self):
        if self.ycor() >= UPPER_LIMIT:
            new_y = self.ycor() + 0
        else:
            new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() <= LOWER_LIMIT:
            new_y = self.ycor() + 0
        else:
            new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
