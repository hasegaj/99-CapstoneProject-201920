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