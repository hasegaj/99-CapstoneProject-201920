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

def guard_quotes():
    list = []

def skyrim(t):
    t = float(t)
    robot = rosebot.RoseBot()
    f = 0

    while True:
        c = robot.sensor_system.color_sensor.get_color()
        if c == 4:
            break
        if c == 5:
            robot.sound_system.beep_for_n_times(5)

        rng1 = robot.sensor_system.ir_proximity_sensor.get_distance()
        rng2 = random.randint(-100,100)

        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.stop()
            # robot.tone_maker.play_sound_file()
            time.sleep(5)
            if f < 7:
                f = f + 1
            else:
                f = f - 7
        if rng1<= 8:
            robot.drive_system.go(-20, -20)
            robot.sound_system.speak_phrase("That is wrong")
            time.sleep(.75)
        if rng2 <= -50:
            robot.drive_system.go(rng2, rng2)
            time.sleep(t)
            robot.drive_system.stop()
        elif rng2>=50:
            robot.drive_system.go(rng2, rng2)
            time.sleep(t)
            robot.drive_system.stop()
        elif rng2 >= 0:
            robot.drive_system.go(rng2, -rng2)
            time.sleep(t)
            robot.drive_system.stop()
        elif rng2 <=0:
            robot.drive_system.go(rng2, -1*rng2)
            time.sleep(t)
            robot.drive_system.stop()

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

