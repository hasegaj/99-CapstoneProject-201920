import time



def beep_move(robot, distance1, speed, dura):
    """
    :type robot: rosebot.RoseBot

    """
    robot.drive_system.go(speed, speed)
    duration = dura
    while True:
        sensor1 = robot.sensor_system.ir_proximity_sensor
        distance = sensor1.get_distance_in_inches()
        robot.sound_system.beeper.beep().wait()
        duration = duration - 1
        if duration <= 1:
            duration = 1
        time.sleep(duration)
        if distance <= distance1:
            break

    robot.drive_system.stop()

def angry_robot(robot,distance,speed, tone, dur, color,second, area, number):
    """
        :type robot: rosebot.RoseBot

        """
    robot.drive_system.go_straight_for_seconds(second,speed)
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    beep_move(robot, distance, speed, dur)
    robot.drive_system.stop()
    robot.sound_system.speak_phrase('Hello, I am Yifan Dai')
    robot.sound_system.beep_for_n_times(number)
    robot.led_left
    robot.led_right
    robot.sound_system.speak_phrase('Error occur, I am angry')
    robot.drive_system.spin(speed, speed).wait()
    while True:
        time.sleep(second)
        break
    robot.sound_system.speak_phrase('I am not angry any more')
    robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
    beep_move(robot, distance, speed, dur)
    robot.arm_and_claw.raise_arm()
    robot.spin(speed, speed).wait()
    while True:
        time.sleep(second)
        break
    robot.drive_system.go_straight_until_color_is(color, speed)
    robot.arm_and_claw.lower_arm()
    robot.sound_system.beep_at_tone(tone, frequency=532)
    robot.sound_system.speak_phrase('Thnank you for wathing')





