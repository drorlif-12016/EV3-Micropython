#!/usr/bin/env python3
import evdev
from evdev import ecodes, InputDevice
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# --- 1. SETUP ---

def find_controller():
    # Use evdev.list_devices() directly to keep imports clean
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "Controller" in device.name:
            return device
    return None


# Connect to motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Connect to controller
gamepad = find_controller()

# Button Constants for readability
BTN_X = 304
BTN_L1 = 310
BTN_R1 = 311

# --- 2. MAIN LOOP ---

if gamepad is not None:
    print(f"Connected to: {gamepad.name}")
    print("Ready! Press X to drive both, or Bumpers to turn.")

    for event in gamepad.read_loop():
        # We only care about Button presses (EV_KEY)
        if event.type == ecodes.EV_KEY:

            # Handle X Button (Both Motors)
            if event.code == BTN_X:
                if event.value == 1:  # Pressed
                    left_motor.run(500)
                    right_motor.run(500)
                else:  # Released
                    left_motor.stop()
                    right_motor.stop()

            # Handle L1 (Left Motor Only)
            elif event.code == BTN_L1:
                if event.value == 1:
                    left_motor.run(500)
                else:
                    left_motor.stop()

            # Handle R1 (Right Motor Only)
            elif event.code == BTN_R1:
                if event.value == 1:
                    right_motor.run(500)
                else:
                    right_motor.stop()
else:
    print("Error: PS4 Controller not found. Is it paired and turned on?")
