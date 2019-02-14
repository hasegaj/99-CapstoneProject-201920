import rosebot
import shared_gui_delegate_on_robot

def go_to_object_and_lift():
    robot = rosebot.RoseBot()
    ir_sensor = rosebot.SensorSystem()
    i_red = ir_sensor.ir_proximity_sensor()
    inches = i_red.get_distance_in_inches()

    robot.drive_system.go()

    while inches >= 1:


        if inches <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
