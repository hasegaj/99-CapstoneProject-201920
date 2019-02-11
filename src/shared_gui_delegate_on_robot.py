"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Josiah Hasegawa, Zeyu Liao, Yifan Dai.
  Winter term, 2018-2019.
"""
class Reciver(object):
    def __init__(self, robot):
        'Type hint: robot: rosebot.RoseBot'
        self.robot = robot
    def forward(self, left_wheel_speed, right_wheel_speed):
        print('forward',left_wheel_speed, right_wheel_speed)
        self.robot.drive_systems.go(int(left_wheel_speed),int(right_wheel_speed))
    def quit(self):
        print('quit')
        self.is_time_to_stop = True
    def beep(self, n):
        print('got beep')
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()
    def stop(self):
        self.robot.drive_systems.go(0,0)

