from turtle import Turtle

MOVE_DIST = 20
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.nag = []
        self.create_snake()
        self.head = self.nag[0]

    def create_snake(self):
        for buss in STARTING_POSITIONS:
            self.add_segments(buss)

    def add_segments(self, pos):
        sss = Turtle(shape="square")
        sss.color("white", "white")
        sss.penup()
        sss.goto(pos)
        self.nag.append(sss)

    def extend(self):
        self.add_segments(self.nag[-1].position())

    def move(self):
        for seg_num in range(len(self.nag)-1, 0, -1):
            new_x = self.nag[seg_num-1].xcor()
            new_y = self.nag[seg_num-1].ycor()
            self.nag[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

