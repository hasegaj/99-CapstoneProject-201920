# Capstone project
# Author: Josiah Hasegawa
import rosebot
import time

def whale(n, k):
    robot = rosebot.RoseBot()
    sensor = robot.sensor_system.ir_proximity_sensor
    robot.drive_system.go(30, 30)
    left = robot.led_left
    right = robot.led_right
    n = float(n)
    k = float(k)
    while True:
        ir = sensor.get_distance()
        left.turn_on()
        left.turn_off()
        time.sleep(k*ir / n)

        right.turn_on()
        right.turn_off()
        time.sleep(k*ir / n)

        left.turn_on()
        right.turn_on()
        left.turn_off()
        right.turn_off()
        time.sleep(k*ir / n)

        if ir <= 3:
            left.set_color_by_name((0, 1))
            right.set_color_by_name((0, 1))
            break
    robot.drive_system.stop()

def skyrim():
    robot = rosebot.RoseBot()
    speak = rosebot.SpeechMaker()
    while robot.sensor_system.color_sensor.get_color() != 'Yellow':
        rng = robot.sensor_system.ir_proximity_sensor.get_distance()


def lotr(n):
    robot = rosebot.RoseBot()
    speak = rosebot.SpeechMaker()

    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<= 20:
            break
    robot.drive_system.go(n, n)

    while True:

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=3:
            robot.drive_system.stop()
            break

    speak.speak('You shall not pass')

def touch_sensor_test():
    robot = rosebot.RoseBot()
    if robot.sensor_system.touch_sensor.is_pressed():
        return 'boop'
