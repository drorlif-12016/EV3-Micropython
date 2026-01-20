#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

ev3 = EV3Brick()
us = UltrasonicSensor(Port.S1)

big = Font(size=20)
ev3.screen.set_font(big)

MAX_DIST = 1000   # max distance in mm shown on graph (1 meter)
BAR_X = 120
BAR_Y = 10
BAR_WIDTH = 30
BAR_HEIGHT = 100

while True:
    ev3.screen.clear()

    # Read distance
    dist = us.distance()

    # Clamp distance to range
    if dist < 0:
        dist = 0
    if dist > MAX_DIST:
        dist = MAX_DIST

    # Convert distance to bar height
    bar = int((dist / MAX_DIST) * BAR_HEIGHT)

    # Draw frame
    ev3.screen.draw_box(BAR_X, BAR_Y, BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT)

    # Draw filled bar (from bottom up)
    ev3.screen.draw_box(
        BAR_X + 2,
        BAR_Y + BAR_HEIGHT - bar,
        BAR_X + BAR_WIDTH - 2,
        BAR_Y + BAR_HEIGHT
    )

    # Draw text
    ev3.screen.draw_text(5, 20, "Distance")
    ev3.screen.draw_text(5, 50, str(dist) + " mm")

    wait(100)
