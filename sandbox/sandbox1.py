# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import rosebot
import time

def flash_lights():
    robot = rosebot.RoseBot().led_system

    d = rosebot.RoseBot().sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while d >= 1:
        robot.left_led.turn_on()
        time.sleep(d)
        robot.left_led.turn_off()
        robot.right_led.turn_on()
        time.sleep(d)
        robot.right_led.turn_off()
        robot.right_led.turn_on()
        robot.left_led.turn_on()
        time.sleep(d)
        robot.right_led.turn_off()
        robot.left_led.turn_off()