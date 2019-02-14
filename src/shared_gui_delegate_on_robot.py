"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Josiah Hasegawa, Zeyu Liao, Yifan Dai. hellow
  Winter term, 2018-2019.1
"""
import liao
import time
class Reciver(object):
    def __init__(self, robot):
        'Type hint: robot: rosebot.RoseBot'
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('GO forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        print('Stop')
        self.robot.drive_system.stop()

    def backward(self,left_wheel_speed, right_wheel_speed):
        print('GO backward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def calibrate_arm(self):
        print('Calibrate arm 2')
        self.robot.arm_and_claw.calibrate_arm()

    def raise_arm(self):
        print('Raise arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('Lower arm')
        self.robot.arm_and_claw.lower_arm()

    def move_arm_to_position(self, position):
        print('Move arm to', int(position))
        self.robot.arm_and_claw.move_arm_to_position(int(position))

    def left(self, left_wheel_speed, right_wheel_speed):
        print('Left', left_wheel_speed, right_wheel_speed)
        Left = int(left_wheel_speed)
        Right = int(right_wheel_speed)
        self.robot.drive_system.go(-Left, Right)

    def right(self, left_wheel_speed, right_wheel_speed):
        print('Right', left_wheel_speed, right_wheel_speed)
        Left = int(left_wheel_speed)
        Right = int(right_wheel_speed)
        self.robot.drive_system.go(Left, -Right)

    def go_straight_for_seconds(self, seconds, speed):
        print('GO straight for second', seconds, speed)
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        print('GO straight for inches', inches, speed)
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        print('GO straight for inches encoder', inches, speed)
        inc = int(inches)
        spe = int(speed)
        self.robot.drive_system.go_straight_for_inches_using_encoder(inc, spe)


    def quit(self):
        print('got quit')
        self.is_time_to_stop = True

    def beep_N(self, n):
        print('Beep')
        N = int(n)
        self.robot.sound_system.beep_for_n_times(N)

    def play_a_tone(self, freq, dur):
        print('play tone')
        self.robot.sound_system.beep_at_tone(int(freq), int(dur))

    def speaker(self, x):
        self.robot.sound_system.speak_phrase(str(x))

    def liao_tone_move(self,seconds,speed, freq, dur, distance):
        frequcence = freq
        while True:
            self.robot.drive_system.go_straight_for_seconds(int(speed),int(seconds))
            self.robot.sound_system.beep_at_tone(int(freq), int(dur))
            frequcence = frequcence + 50
            if distance <= 1:
                break
        self.robot.drive_system.stop()
        self.stop()





