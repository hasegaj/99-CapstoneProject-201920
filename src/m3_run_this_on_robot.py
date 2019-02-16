"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
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
    #test()
    #spin()
    #F_stuff()
    angry_robot()

def real_thing():
    robot = rosebot.RoseBot()
    reciever = rec.Reciver(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(.01)

def test():
    robot = rosebot.RoseBot()
    robot.drive_system.display_camera_data()

def spin():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_counterclockwise_until_sees_object(100,2500)

def F_stuff():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(2,50)


def angry_robot():
    angry_robot1()
    angry_robot2()
    angry_robot3()
    angry_robot4()
    angry_robot5()
    angry_robot6()




def angry_robot1():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_clockwise_until_sees_object(100,2500)

def angry_robot2():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(1,200)

def angry_robot3():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(0.2,50)
    robot.drive_system.go(-500,500).wait(200)
    robot.drive_system.stop()

def angry_robot4():
    robot = rosebot.RoseBot()
    robot.sound_system.speak_phrase('Hello')
    robot.sound_system.speak_phrase('I am Yifan Dai')
    robot.sound_system.speak_phrase('I am angry')
    robot.sound_system.beep_for_n_times(20).wait(10)

def angry_robot5():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.move_arm_to_position(2500)
    robot.sound_system.beep_at_tone(600,50).wait(2)
    robot.sound_system.speak_phrase('angry bots is back')
    robot.drive_system.go(500, -500)
    robot.drive_system.stop()
    robot.arm_and_claw.move_arm_to_position(0)

def angry_robot6():
    robot = rosebot.RoseBot()
    robot.sound_system.speak_phrase('I am not angry anymore')
    robot.drive_system.spin_clockwise_until_sees_object(50, 2500)












# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()