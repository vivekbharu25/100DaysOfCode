import turtle as t
import random

jim = t.Turtle()
jim.shape("arrow")
t.colormode(255)

def random_color():
    r  = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors  = (r,g,b)
    return colors

angles  = [90,180,270,360]
jim.speed("fastest")

for i in range(100):
    angle = 360/100
    jim.color(random_color())
    jim.right(angle)
    jim.circle(100)


screen = t.Screen()
screen.exitonclick()