"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zeyu Liao.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time
import rosebot

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
    frame_label = ttk.Label(frame, text="廖")
    speed_label = ttk.Label(frame, text="wheel speed (0 to 100)")
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    second_lable = ttk.Label(frame, text="second")
    second_entry = ttk.Entry(frame, width=5, justify=tkinter.LEFT)
    freq_label = ttk.Label(frame, text="freq")
    freq_entry = ttk.Entry(frame, width=8,justify=tkinter.LEFT)
    dur_label = ttk.Label(frame, text="dur")
    dur_entry = ttk.Entry(frame, width=4, justify=tkinter.LEFT)
    Tone_button = ttk.Button(frame, text='Move tone!')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=2, column=1)
    second_lable.grid(row=5, column=2)
    second_entry.grid(row=5, column=3, sticky='w')
    freq_label.grid(row=3, column=0)
    freq_entry.grid(row=3, column=1)
    dur_label.grid(row=5, column=0)
    dur_entry.grid(row=5, column=1)
    Tone_button.grid(row=3, column=3)
    # Set the button callbacks:
    Tone_button["command"] = lambda: handle_tone_move(second_entry,speed_entry,freq_entry,dur_entry,mqtt_sender)

    return frame

def handle_tone_move(seconds,speed,fren,dur,mqtt_sender):
    print('M+T')
    mqtt_sender.send_message('tone_move',[seconds.get(), speed.get(),fren.get(),dur.get()])