"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Zeyu Liao.
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
    real_thing()
    # something()
    # raise_arm()

def real_thing():
    robot = rosebot.RoseBot()
    reciver = rec.Reciver(robot)
    mqtt_reciver = com.MqttClient(reciver)
    mqtt_reciver.connect_to_pc()

    while True:
        time.sleep(0.01)


# def something():
#     robot= rosebot.RoseBot()
#     robot.arm_and_claw.calibrate_arm()
#     robot.drive_system.Toone_move()
#
# def raise_arm():
#     robot = rosebot.RoseBot()
#     robot.drive_system.Toone_move()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()