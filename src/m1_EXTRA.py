# Capstone project
# Author: Josiah Hasegawa
import rosebot
import shared_gui_delegate_on_robot
import tkinter
from tkinter import ttk

def get_guard_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Guard")
    lotr_label = ttk.Label(frame, text="gandalf")
    skyrim_label = ttk.Label(frame, text="skyrim guard")

    lotr_button = ttk.Button(frame, text="gandalf")
    skyrim_button = ttk.Button(frame, text="skyrim guard")

    #grid widgits
    frame_label.grid(row=0, column=1)
    lotr_label.grid(row=3, column=0)
    skyrim_label.grid(row=4, column=0)

    lotr_button.grid(row=3, column=1)
    skyrim_button.grid(row=4, column=1)

    #button callbacks
    #lotr_button["command"]= lambda:
    #skyrim_button["command"] = lambda:

    return frame

def get_feature_10_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=6, borderwidth=7, relief="ridge")
    frame.grid()


