"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Josiah Hasegawa.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #real_thing()
    #F_stuff()
    #light_cycle()

    flash_lights()

def real_thing():
    robot = rosebot.RoseBot()
    reciever = rec.Reciver(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(.01)

def F_stuff():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(2, 50)

def light_cycle():
    robot = rosebot.RoseBot().led_system
    robot.left_led.turn_on()
    time.sleep(1)
    robot.left_led.turn_off()
    robot.right_led.turn_on()
    time.sleep(1)
    robot.right_led.turn_off()
    robot.right_led.turn_on()
    robot.left_led.turn_on()
    time.sleep(1)
    robot.right_led.turn_off()
    robot.left_led.turn_off()


def flash_lights():
    robot = rosebot.RoseBot().led_system
    r = rosebot.RoseBot().sensor_system.ir_proximity_sensor
    while True:

        if r.get_distance_in_inches() >= 1:
            robot.left_led.turn_on()
            robot.left_led.turn_off()
            time.sleep(r.get_distance_in_inches() / 20)

            robot.right_led.turn_on()
            robot.right_led.turn_off()
            time.sleep(r.get_distance_in_inches() / 20)

            robot.right_led.turn_on()
            robot.left_led.turn_on()

            robot.right_led.turn_off()
            robot.left_led.turn_off()
            time.sleep(r.get_distance_in_inches() / 20)

        if r.get_distance_in_inches() <= 1:
            robot.right_led.turn_off()
            robot.left_led.turn_off()
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()