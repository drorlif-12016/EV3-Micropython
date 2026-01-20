#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# intialize the EV3 brick
ev3 = EV3Brick()

# Calls the motors and the gyro
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S2)


wheel_diameter = 20
axle_track = 144


class PIDDrive:

    def __init__(self, left_motor, right_motor,
                 wheel_diameter, axle_track, gyro=None):
        self.left = left_motor
        self.right = right_motor
        self.gyro = gyro

        # Robot geometry
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

        # PID constants (you WILL tune these)
        self.kp_dist = 1.2
        self.ki_dist = 0.0
        self.kd_dist = 0.2

        self.kp_head = 3.0
        self.ki_head = 0.0
        self.kd_head = 0.4

    # Reset encoders
    def reset(self):
        self.left.reset_angle(0)
        self.right.reset_angle(0)
        if self.gyro:
            self.gyro.reset_angle(0)

    # Convert mm to motor degrees
    def mm_to_deg(self, mm):
        wheel_circ = 3.1416 * self.wheel_diameter
        return (mm / wheel_circ) * 360

    # Drive straight with PID + heading correction
    def drive(self, distance_mm, max_speed=300):
        target = self.mm_to_deg(distance_mm)

        self.reset()

        error_prev = 0
        integral = 0

        heading_target = 0
        if self.gyro:
            heading_target = self.gyro.angle()

        while True:
            # Current distance (average of both motors)
            pos = (self.left.angle() + self.right.angle()) / 2
            error = target - pos

            # Stop condition
            if abs(error) < 5:
                break

            # Distance PID
            integral += error
            derivative = error - error_prev
            error_prev = error

            forward = (
                self.kp_dist * error +
                self.ki_dist * integral +
                self.kd_dist * derivative
            )

            # Limit speed
            if forward > max_speed:
                forward = max_speed
            if forward < -max_speed:
                forward = -max_speed

            # Heading correction
            correction = 0
            if self.gyro:
                heading_error = heading_target - self.gyro.angle()
                correction = self.kp_head * heading_error

            # Apply to motors
            self.left.run(forward + correction)
            self.right.run(forward - correction)

            wait(10)

        self.left.stop()
        self.right.stop()

    # Turn in place using gyro PID
    def turn(self, angle_deg, max_speed=200):
        if not self.gyro:
            raise Exception("Gyro required for PID turning")

        self.gyro.reset_angle(0)

        error_prev = 0
        integral = 0

        while True:
            error = angle_deg - self.gyro.angle()

            if abs(error) < 1:
                break

            integral += error
            derivative = error - error_prev
            error_prev = error

            turn = (
                self.kp_head * error +
                self.ki_head * integral +
                self.kd_head * derivative
            )

            # Limit
            if turn > max_speed:
                turn = max_speed
            if turn < -max_speed:
                turn = -max_speed

            self.left.run(turn)
            self.right.run(-turn)

            wait(10)

        self.left.stop()
        self.right.stop()
