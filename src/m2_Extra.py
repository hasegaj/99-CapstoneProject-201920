"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zeyu Liao.
  Winter term, 2018-2019.
"""
import tkinter
from tkinter import ttk
from tkinter import *

def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Treasure hunting")
    speed_label = ttk.Label(frame, text="wheel speed (0 to 100)")
    speed_entry = ttk.Entry(frame, width=8)
    start_button = ttk.Button(frame, text='Start!')
    lower_button = ttk.Button(frame, text='Lower arm!')
    left_button = ttk.Button(frame, text='Left')
    right_button = ttk.Button(frame, text='Right!')
    stop_button = ttk.Button(frame, text='Stop!')
    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    speed_label.grid(row=0, column=1)
    speed_entry.grid(row=1, column=1)
    start_button.grid(row=0, column=2)
    lower_button.grid(row=2, column=2)
    left_button.grid(row=0,column=3)
    stop_button.grid(row=1,column=3)
    right_button.grid(row=2,column=3)
    # Set the button callbacks:
    start_button["command"] = lambda: handle_hunting(speed_entry,mqtt_sender)
    lower_button["command"] = lambda:lower_arm(mqtt_sender)
    left_button["command"] = lambda:handle_left(speed_entry,mqtt_sender)
    stop_button["command"] = lambda :handle_stop(mqtt_sender)
    right_button["command"] = lambda: handle_right(speed_entry,mqtt_sender)
    return frame

def handle_hunting(speed,mqtt_sender):
    print('M+T')
    mqtt_sender.send_message("m2_Extra_hunting",[speed.get()])

def lower_arm(mqtt_sender):
    mqtt_sender.send_message("lower_arm")

def handle_left(speed_entry, mqtt_sender):
    mqtt_sender.send_message("left", [speed_entry.get(), speed_entry.get()])

def handle_right(speed_entry, mqtt_sender):

    mqtt_sender.send_message("right", [speed_entry.get(), speed_entry.get()])

def handle_stop(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message("stop")