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
    while robot.sensor_system.color_sensor.get_color() != 4:
        rng1 = robot.sensor_system.ir_proximity_sensor.get_distance()
        rng2 = robot.drive_system.right_motor.get_position()
        rng3 = robot.drive_system.left_motor.get_position()
        if robot.sensor_system.touch_sensor.is_pressed():
            robot.tone_maker.play_sound_file()

        if (rng1 + rng2 + rng3) % 2==0:
            robot.drive_system.go()
            time.sleep()
            robot.drive_system.stop()
        elif (rng1 + rng2 + rng3) % 2 !=0:
            robot.drive_system.go()
            time.sleep()
            robot.drive_system.stop()


def guard_quotes():
    list = []
def lotr(n):
    robot = rosebot.RoseBot()
    speak = rosebot.SpeechMaker()
    n = float(n)

    while True:
        time.sleep(.5)

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<= 15:
            robot.drive_system.go(n, n)
            break

    while True:

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=5:
            robot.drive_system.stop()
            break

    speak.speak('You shall not pass')
    time.sleep(1)


def touch_sensor_test():
    robot = rosebot.RoseBot()
    if robot.sensor_system.touch_sensor.is_pressed():
        return 'boop'

