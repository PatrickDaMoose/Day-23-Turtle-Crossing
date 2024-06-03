# Udemy's 100 days of Code - Python Bootcamp
# Day 23 Capstone Project - Turtle Crossing
# By Patrick Morse

# Goal: To emulate a frogger style game using the Turtle Graphics package.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen set up, initialize class, set size.
# Set screen to update on call, and to listen for events
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Variable defined for later use
sleep_value = 0.1

# Player initialization and initial position set. see /player.py
player = Player()
player.reset_pos()

# Scoreboard initialization. see /scoreboard.py
scoreboard = Scoreboard()

# Call player methods on key press/hold
screen.onkeypress(player.m_forward, "Up")
screen.onkeypress(player.m_backward, "Down")

# Start loop and initialize a CarManager object. see /car_manager.py
game_is_on = True
car = CarManager()

while game_is_on:
    # Method for adding cars multiplied by level value
    car.add_car()
    car.move()
    # Screen update call based on sleep_value variable
    time.sleep(sleep_value)
    screen.update()

    # Level Win
    # Adds an increment to level variable, increasing cars. Speeds screen updates up slightly.
    if player.ycor() > 280:
        player.reset_pos()
        scoreboard.level_up()
        car.level_up()
        sleep_value *= 0.9

    # Collision Detection
    # Methods for ending game and fail/lose conditions. Closes loop on fail.
    for value in car.obj_list:
        if player.distance(value) < 15:
            scoreboard.game_over()
            player.reset_pos()
            game_is_on = False

screen.exitonclick()
