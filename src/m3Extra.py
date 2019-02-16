import tkinter
from tkinter import ttk


def get_teleoperation_frame(window, mqtt_sender):

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

def handle_beep_move(distance1, speed, dur, mqtt_sender):
    print('beep move')
    mqtt_sender.send_message('beep_move',[distance1.get(), speed.get(),dur.get()])