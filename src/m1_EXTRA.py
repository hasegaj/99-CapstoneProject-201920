# Capstone project
# Author: Josiah Hasegawa
import rosebot
import time
import random

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

def skyrim(t, k, m):
    t = float(t)
    k = float(k)
    m = float(m)
    robot = rosebot.RoseBot()
    list = ["I used to", "be an adventurer", "like you", "but then",
            "I took an", "arrow in the knee"]
    while True:
        c = robot.sensor_system.color_sensor.get_color()
        robot.sensor_system.color_sensor.get_color()
        if c == 4:
            break
        if c == m:
            robot.sound_system.beep_for_n_times(m+1)
            break

        rng1 = robot.sensor_system.ir_proximity_sensor.get_distance()
        rng2 = random.randint(-100,100)

        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.stop()
            for k in range(len(list)):
                robot.sound_system.speak_phrase(list[k])
                time.sleep(1.5)
            robot.drive_system.go(40, 40)
            time.sleep(.6)
            robot.drive_system.stop()

        if rng1<= 8:
            robot.drive_system.go(-100, -100)
            robot.sound_system.speak_phrase("That is wrong")
            time.sleep(.75)
        if rng2 <= -50:
            robot.drive_system.go(-k, -k)
            time.sleep(t)
            robot.drive_system.stop()
        elif rng2>=50:
            robot.drive_system.go(k, k)
            time.sleep(t)
            robot.drive_system.stop()
        elif rng2 >= 0:
            robot.drive_system.go(k, -k)
            time.sleep(t*1.25)
            robot.drive_system.stop()
        elif rng2 <=0:
            robot.drive_system.go(-k, k)
            time.sleep(t*1.25)
            robot.drive_system.stop()

def lotr(n):
    robot = rosebot.RoseBot()
    speak = rosebot.SpeechMaker()
    n = float(n)

    while True:
        time.sleep(.5)

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<= 12:
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

