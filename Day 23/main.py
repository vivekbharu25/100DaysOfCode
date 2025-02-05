import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scores = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")



game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop+=1
    if loop%6 ==0:
        cars.car_gen()
    cars.movement()

    for car in cars.cars:
        if car.distance(turtle) < 22:
            scores.game_over()
            game_is_on = False

    if turtle.is_at_finish():
        turtle.go_start()
        cars.level_up()
        scores.update_score()




screen.exitonclick()