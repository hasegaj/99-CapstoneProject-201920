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
    real_thing()
    #F_stuff()
    #light_cycle()
    #flash_lights()
    #merp = rosebot.RoseBot()
    #merp.drive_system.Toone_move(5, 30, .2, 400)
    #whale()

def real_thing():
    robot = rosebot.RoseBot()
    reciever = rec.Reciver(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(.01)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()