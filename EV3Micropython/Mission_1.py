#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.media.ev3dev import Font


# Initialize the EV3 Brick.
ev3 = EV3Brick()

big = Font(size=24)
small = Font(size=12)
ev3.screen.set_font(big)

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
robot.straight(1000)
robot.straight(-1000)

# robot Turn by 360 degrees and back again.
# robot.turn(360)
# robot.turn(-360)

while True:
    ev3.screen.clear()
    ev3.screen.draw_text(12, 50, "Distence: " + str(robot.distance()))
    wait(100)
