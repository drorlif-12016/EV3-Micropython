#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
import math

ev3 = EV3Brick()
us = UltrasonicSensor(Port.S1)
motor = Motor(Port.B)

WIDTH = 178
HEIGHT = 128
MAX_DIST = 1000   # mm

graph = [0] * WIDTH
x = 0

# Oscillation parameters
AMPLITUDE = 200    # motor speed (deg/s)
OMEGA = 0.15       # oscillation speed
t = 0              # phase


while True:
    # -----------------------------
    # Motor oscillation
    # -----------------------------
    speed = int(AMPLITUDE * math.sin(t))
    motor.run(speed)
    t += OMEGA

    # -----------------------------
    # Read distance
    # -----------------------------
    dist = us.distance()
    if dist < 0:
        dist = 0
    if dist > MAX_DIST:
        dist = MAX_DIST

    # Convert distance to screen Y (inverted)
    y = int((dist / MAX_DIST) * (HEIGHT - 20))
    y = HEIGHT - 1 - y

    # Store in history
    graph[x] = y

    # -----------------------------
    # Draw graph
    # -----------------------------
    ev3.screen.clear()
    ev3.screen.draw_line(0, HEIGHT - 20, WIDTH, HEIGHT - 20)

    for i in range(1, x):
        y1 = graph[i - 1]
        y2 = graph[i]

        # Main line
        ev3.screen.draw_line(i - 1, y1, i, y2)

        # Thickness (3 px)
        ev3.screen.draw_line(i - 1, y1 + 1, i, y2 + 1)
        ev3.screen.draw_line(i - 1, y1 - 1, i, y2 - 1)

    # -----------------------------
    # Advance graph
    # -----------------------------
    x += 1
    if x >= WIDTH:
        x = 0
        graph = [0] * WIDTH

    wait(50)
