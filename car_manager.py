import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Initializes Car Orchestration. callable methods, add_car, move, and level_up"""
    def __init__(self):
        self.level = 1
        self.car_number = 0
        self.obj_list = []
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    # Car Generation:
    # Checks if object list is less than level * 10
    # Defines a new random y and color
    # Creates a turtle stretched to a rectangle, and sends to random y
    # Appends turtle to list for move through iteration
    def add_car(self):
        if len(self.obj_list) <= ((self.level * 10) - int(self.level * 1.5)):
            self.new_y = random.randint(-240, 240)
            self.rcolor = random.choice(COLORS)
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.color(self.rcolor)
            tim.shapesize(stretch_wid=1, stretch_len=2.5)
            tim.goto(290, self.new_y)
            tim.seth(180)
            self.obj_list.append(tim)
        else:
            pass

    # Move method:
    # Iterates through self.obj_list to move each object to a random x, 0-25 value.
    # If car reaches edge of screen, or -280, call reset_car method
    def move(self):
        for value in self.obj_list:
            rand_x = random.randint(0, 25)
            new_x = value.xcor() - rand_x
            value.goto(new_x, value.ycor())
            if value.xcor() < -280:
                self.reset_car(value)

    # Internal method for "clearing" old objects and resetting the loop
    def reset_car(self, obj):
        obj.hideturtle()
        self.obj_list.remove(obj)
        self.add_car()

    # Adds a level variable, increasing the amount of cars spawned to get through.
    def level_up(self):
        self.level += 1
