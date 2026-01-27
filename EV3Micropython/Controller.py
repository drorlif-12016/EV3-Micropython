#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from evdev import InputDevice, ecodes

# Initialize motor and controller
left_motor = Motor(Port.B)
Right_motor = Motor(Port.C)
gamepad = InputDevice('/dev/input/event0')  # This path varies

# Listen for events
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.code == 304:  # The 'X' button code
            if event.value == 1:  # Button Pressed
                left_motor.run(500)
                Right_motor.run(500)
            else:  # Button Released
                left_motor.stop()
