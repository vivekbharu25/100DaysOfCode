import turtle
from turtle import Turtle, Screen

kurma = Turtle()
screen = Screen()

def move_forwards():
    kurma.forward(20)
def move_backwards():
    kurma.backward(20)
def move_cw():
    kurma.left(10)
def move_ccw():
        kurma.right(10)

screen.listen()
screen.onkey(key = "w", fun=move_forwards)
screen.onkey(key = "s", fun=move_backwards)
screen.onkey(key = "a", fun=move_cw)
screen.onkey(key = "d", fun=move_ccw)
screen.onkey(key = "c", fun=turtle.resetscreen)
screen.exitonclick()