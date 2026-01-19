#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

# Veriables and intialization of Devices
ev3 = EV3Brick()
UltraSonic = UltrasonicSensor(Port.S1)

big = Font(size=24)
small = Font(size=12)
ev3.screen.set_font(big)

# operations
ev3.speaker.beep()
while True:
    ev3.screen.clear()
    ev3.screen.draw_text(12, 50, "Distence: " + str(UltraSonic.distance()))
    wait(100)
