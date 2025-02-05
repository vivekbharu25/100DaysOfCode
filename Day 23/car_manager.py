from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def car_gen(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setpos(310, random.randint(-230, 230))
        self.cars.append(car)

    def movement(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

