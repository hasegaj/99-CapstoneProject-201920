"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Yifan Dai.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui




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
    teleop_frame, arm_frame, control_frame, sound_frame, drive_frame, m3Extra_frame, angry_frame = get_shared_frames(main_frame,mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    get_newteleoperation_frame(main_frame, mqtt_sender)
    angry_robot_frame(main_frame,mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, drive_frame, m3Extra_frame, angry_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame , mqtt_sender,)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame,mqtt_sender)
    sound_frame = shared_gui.get_soundsystem_frame(main_frame,mqtt_sender)
    drive_frame = shared_gui.get_drivesystem_frame(main_frame,mqtt_sender)
    m3Extra_frame = get_newteleoperation_frame(main_frame,mqtt_sender)
    angry_frame = angry_robot_frame(main_frame,mqtt_sender)
    return teleop_frame, arm_frame, control_frame, sound_frame, drive_frame, m3Extra_frame,angry_frame

def grid_frames(teleop_frame, arm_frame, control_frame, sound_frame, drive_frame, m3Extra_frame, angry_frame):
    teleop_frame.grid(row = 0, column = 0)
    arm_frame.grid(row = 0, column = 1)
    control_frame.grid(row = 1, column = 1)
    sound_frame.grid(row = 3, column = 0)
    drive_frame.grid(row = 3, column = 1)
    m3Extra_frame.grid(row = 4, column = 0)
    angry_frame.grid(row=4, column=1)

def get_newteleoperation_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="GodDzZ")
    speed_label = ttk.Label(frame, text="wheel speed (0 to 100)")
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    distance_label = ttk.Label(frame, text="distance")
    distance_entry = ttk.Entry(frame, width=5, justify=tkinter.LEFT)

    dur_label = ttk.Label(frame, text="dur")
    dur_entry = ttk.Entry(frame, width=4, justify=tkinter.LEFT)
    beep_button = ttk.Button(frame, text='Move beep!')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=2, column=1)
    distance_label.grid(row=2, column=2)
    distance_entry.grid(row=2, column=3, sticky='w')

    dur_label.grid(row=4, column=0)
    dur_entry.grid(row=4, column=1)
    beep_button.grid(row=3, column=3)
    # Set the button callbacks:
    beep_button["command"] = lambda: handle_beep_move(distance_entry,speed_entry,dur_entry,mqtt_sender)

    return frame

def angry_robot_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="GodDzZ-angry")
    speed_label = ttk.Label(frame, text="wheel speed (0 to 100)")
    speed_entry = ttk.Entry(frame, width=4)
    distance_label = ttk.Label(frame, text="distance")
    distance_entry = ttk.Entry(frame, width=4, justify=tkinter.LEFT)
    tone_label = ttk.Label(frame, text='tone')
    tone_entry = ttk.Entry(frame, width=4,justify=tkinter.LEFT )
    dur_label = ttk.Label(frame, text="dur")
    dur_entry = ttk.Entry(frame, width=4, justify=tkinter.LEFT)
    color_label = ttk.Label(frame, text='color')
    color_entry = ttk.Entry(frame, width=4)
    second_label = ttk.Label(frame, text='second')
    second_entry = ttk.Entry(frame, width=4)
    number_label = ttk.Label(frame, text='number')
    number_entry = ttk.Entry(frame, width=4)
    area_label = ttk.Label(frame, text='area')
    area_entry =ttk.Entry(frame, width=4)
    angry_robot_button = ttk.Button(frame, text='Become angry')

    # Grid the widgets:
    frame_label.grid(row=0, column=2)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=1, column=1)
    distance_label.grid(row=2, column=0)
    distance_entry.grid(row=2, column=1)
    tone_label.grid(row = 3, column = 0)
    tone_entry.grid(row=3, column=1)
    color_label.grid(row = 4, column = 0)
    color_entry.grid(row=4, column=1)
    second_label.grid(row = 5, column = 0)
    second_entry.grid(row=5, column=1)
    area_label.grid(row=6, column=0)
    area_entry.grid(row = 6, column = 1)
    number_label.grid(row = 7, column =0)
    number_entry.grid(row=7, column=1)
    dur_label.grid(row=8, column=0)
    dur_entry.grid(row=8, column=1)
    angry_robot_button.grid(row=3, column=3)
    # Set the button callbacks:
    angry_robot_button["command"] = lambda: handle_angry_robot(distance_entry,speed_entry, tone_entry, dur_entry, color_entry,second_entry, area_entry, number_entry,mqtt_sender)

    return frame






def handle_beep_move(distance1, speed, dur, mqtt_sender):
    print('beep move')
    mqtt_sender.send_message('beep_move',[distance1.get(), speed.get(),dur.get()])

def handle_angry_robot(distance,speed, tone, dur, color,second, area, number,mqtt_sender):
    print('angry robot')
    mqtt_sender.send_message('angry robot', distance.get(),speed.get(), tone.get(), dur.get(), color.get(),second.get(), area.get(), number.get())
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()