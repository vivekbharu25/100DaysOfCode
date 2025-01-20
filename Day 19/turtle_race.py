import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=1500, height=1200)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
x = -730
y = -99
turtles = []

for i in colors:
    t = Turtle(shape="turtle")
    t.color(i)
    t.penup()
    t.goto(x,y)
    y+=33

    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in turtles:
        if i.xcor()>730:
            is_race_on = False
            winner_color = i.pencolor()
            if winner_color == user_bet:
                print(f"You've won. The {winner_color} is the winner!")
            else:
                print(f"You've lost. The {winner_color} is the winner!")
        i.forward(random.randint(0,10))

screen.exitonclick()
