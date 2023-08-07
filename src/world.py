import dearpygui.dearpygui as dpg
import json


def world_callback():
    with dpg.window(label="World", tag="world_window"):
        dpg.add_button(label="Player Types")
        dpg.add_button(label="Dialogues")
        dpg.add_button(label="Shops")
        dpg.add_button(label="Global Variables")
