# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import ev3dev.ev3 as ev3
import time
import math
def go_straight_until_intensity_is_less_than(self, intensity, speed):
    """
    Goes straight at the given speed until the intensity returned
    by the color_sensor is less than the given intensity.
    """
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.ColorSensor()
        if sensor.reflected_light_intensity <= intensity:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_intensity_is_greater_than(self, intensity, speed):
    """
    Goes straight at the given speed until the intensity returned
    by the color_sensor is greater than the given intensity.
    """
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.ColorSensor()
        if sensor.reflected_light_intensity >= intensity:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_color_is(self, color, speed):
    """
    Goes straight at the given speed until the color returned
    by the color_sensor is equal to the given color.
    """
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.ColorSensor()
        num = int(sensor.color)
        if num == color:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_straight_until_color_is_not(self, color, speed):
    """
    Goes straight at the given speed until the color returned
    by the color_sensor is NOT equal to the given color.
    """

    # -------------------------------------------------------------------------
    # Methods for driving that use the infrared proximity sensor.
    # -------------------------------------------------------------------------
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.ColorSensor()
        num = int(sensor.color)
        if num != color:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_forward_until_distance_is_less_than(self, inches, speed):
    """
    Goes forward at the given speed until the robot is less than
    the given number of inches from the nearest object that it senses.
    """
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.InfraredSensor()
        num = int(sensor.proximity)*0.7
        if num <= inches*2.54:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_backward_until_distance_is_greater_than(self, inches, speed):
    """
    Goes straight at the given speed until the robot is greater than
    the given number of inches from the nearest object that it senses.
    Assumes that it senses an object when it starts.
    """
    self.left_motor.turn_on(speed)
    self.right_motor.turn_on(speed)
    while True:
        sensor = ev3.InfraredSensor()
        num = int(sensor.proximity) * 0.7
        if num >= inches * 2.54:
            print('OK')
            break
    self.left_motor.turn_off()
    self.right_motor.turn_off()


def go_until_distance_is_within(self, delta_inches, speed):
    """
    Goes forward or backward, repeated as necessary, until the robot is
    within the given delt
    """
    sensor = ev3.InfraredSensor()
    num = int(sensor.proximity) * 0.7
    if num >= delta_inches * 2.54:
       go_forward_until_distance_is_less_than(self,delta_inches,speed)
    if num <= delta_inches * 2.54:
        go_backward_until_distance_is_greater_than(self,delta_inches,speed)
