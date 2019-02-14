"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zeyu Liao.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import liao



def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE120 Capstone Project, Winter 2018-19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 5, relief = "groove")
    main_frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame,control_frame, sound_frame, drive_frame, liao_frame = get_shared_frames(main_frame,mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    #DO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, drive_frame,liao_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame , mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_fram = shared_gui.get_control_frame(main_frame,mqtt_sender)
    sound_frame = shared_gui.get_soundsystem_frame(main_frame,mqtt_sender)
    drive_frame = shared_gui.get_drivesystem_frame(main_frame,mqtt_sender)
    liao_frame = liao.get_teleoperation_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_fram, sound_frame, drive_frame, liao_frame

def grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, drive_frame,liao_frame):
    teleop_frame.grid(row= 0, column = 0)
    arm_frame.grid(row= 0, column = 1)
    control_frame.grid(row= 1, column = 1)
    sound_frame.grid(row= 3, column = 0)
    drive_frame.grid(row= 3, column = 1)
    liao_frame.grid(row= 4, column = 1)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()