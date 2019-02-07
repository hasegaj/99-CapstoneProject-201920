"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Josiah Hasegawa, Zeyu Liao, Yifan Dai.
  Winter term, 2018-2019.
"""

class Receiver(object):
    def __init__(self, robot):
        self.robot = robot

        def forward(self, left_wheel_speed, right_wheel_speed):
            print("God foward", left_wheel_speed, right_wheel_speed)
            self.robot.drive_system.go(int(left_wheel_speed),
                                       int(right_wheel_speed))