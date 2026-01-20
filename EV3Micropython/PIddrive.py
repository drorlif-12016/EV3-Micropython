#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Create drive base (wheel_diameter and axle_track in mm)
robot = DriveBase(left_motor, right_motor,
                  wheel_diameter=56,
                  axle_track=114)

# Stop robot before changing PID
robot.stop()

# Tune PID for driving straight (distance control)
robot.distance_control.pid(
    kp=10,
    ki=2,
    kd=1,
    integral_range=20,
    integral_rate=100,
    feed_forward=15
)

# Tune PID for turning (heading control)
robot.heading_control.pid(
    kp=8,
    ki=1,
    kd=2,
    integral_range=20,
    integral_rate=100,
    feed_forward=10
)

# Drive forward 300 mm accurately
robot.straight(300)
wait(3000)

# Turn 90 degrees accurately
robot.turn(90)
wait(3000)

robot.stop()

while True:
    ev3.screen.clear()
    ev3.screen.draw_text(12, 50, "Distence: " + str(robot.distance()))
    wait(100)
