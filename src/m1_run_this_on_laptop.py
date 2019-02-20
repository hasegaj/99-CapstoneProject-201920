"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Josiah Hasegawa.
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
    root.title("whatever title i want")
    root.configure(bg="#ff0088")
    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=1, borderwidth=6, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, test_frame, sound_frame, \
     new_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, test_frame, sound_frame,
                new_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

def sprint_3_GUI():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("some title")
    root.geometry('400x300')
    root.configure(bg="#0099cd")
    main_frame = ttk.Frame(root, padding=1, borderwidth=10, relief='groove')
    main_frame.pack()
    guard_frame = get_guard_frame(main_frame, mqtt_sender)
    grid_2(guard_frame)

    root.mainloop()

def get_guard_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Guard")
    lotr_label = ttk.Label(frame, text="gandalf")
    skyrim_label = ttk.Label(frame, text="skyrim guard")

    lotr_button = ttk.Button(frame, text="gandalf")
    skyrim_button = ttk.Button(frame, text="skyrim guard")

    lotr_entry = ttk.Entry(frame, width=5)
    lotr_entry.insert(0, '30')
    skyrim_entry = ttk.Entry(frame, width=5)
    skyrim_entry.insert(0, '.5')
    skyrim_entry2 = ttk.Entry(frame, width=5)
    skyrim_entry3 = ttk.Entry(frame, width=5)
    skyrim_label2 = ttk.Label(frame, text="speed(-100-100)")
    skyrim_entry2.insert(0, "40")
    skyrim_label3 = ttk.Label(frame, text="color(0-7)")
    skyrim_entry3.insert(0, "5")
    #grid widgits
    frame_label.grid(row=0, column=1)
    lotr_label.grid(row=3, column=0)
    skyrim_label.grid(row=4, column=0)
    lotr_entry.grid(row=3, column=2)
    lotr_button.grid(row=3, column=1)
    skyrim_button.grid(row=4, column=1)
    skyrim_entry.grid(row=4, column=2)
    skyrim_entry2.grid(row=5, column=2)
    skyrim_entry3.grid(row=6, column=2)
    skyrim_label2.grid(row=5, column=1)
    skyrim_label3.grid(row=6, column=1)
    #button callbacks
    lotr_button["command"]= lambda: shared_gui.handle_lotr(lotr_entry, mqtt_sender)
    skyrim_button["command"] = lambda: shared_gui.handle_skyrim(skyrim_entry, skyrim_entry2, skyrim_entry3, mqtt_sender)

    return frame

def get_object_while_blinking(window, mqtt_sender):
    frame = ttk.Frame(window, padding=1, borderwidth=4, relief="ridge")
    frame.grid()

    label = ttk.Label(frame, text="pick up object while flashing")
    button = ttk.Button(frame, text="ugh")
    entry = ttk.Entry(frame, width=5)
    entry2 = ttk.Entry(frame, width=5)
    entry2.insert(0, '1')

    label.grid(row=1, column=1)
    button.grid(row=1, column=2)
    entry.grid(row=1, column=3)
    entry2.grid(row=2, column=3)

    button["command"]= lambda: shared_gui.handle_ugh(entry, entry2, mqtt_sender)
    return frame

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    test_frame = shared_gui.get_drivesystem_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_soundsystem_frame(main_frame, mqtt_sender)
    new_frame = get_object_while_blinking(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, test_frame, sound_frame, new_frame

def get_frame_2(main_frame, mqtt_sender):
    guard_frame = get_guard_frame(main_frame, mqtt_sender)

    return guard_frame

def grid_frames(teleop_frame, arm_frame, control_frame, test_frame, sound_frame, new_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    test_frame.grid(row=0, column=1)
    sound_frame.grid(row=1, column=1)
    new_frame.grid(row=2, column=1)

def grid_2(guard_frame):
    guard_frame.grid(row=1, column=1)

def title_window():

    root = tkinter.Tk()
    root.title("Starting GUI")
    root.geometry('400x200+500+300')
    root.configure(bg="#0099cd")
    main_frame = ttk.Frame(root, padding=1, borderwidth=15, relief='groove')

    main_frame.pack()

    this = get_this_frame(main_frame)
    this.grid()

    root.mainloop()

def get_this_frame(window):
    frame = ttk.Frame(window)
    frame.grid()
    button1 = ttk.Button(frame, text="team window")
    button2 = ttk.Button(frame, text="sprint 3 window")
    button1["command"] = lambda: main()
    button2["command"] = lambda: sprint_3_GUI()
    button1.grid()
    button2.grid()
    return frame
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
#main()
#sprint_3_GUI()
title_window()