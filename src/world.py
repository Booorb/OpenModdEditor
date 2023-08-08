import dearpygui.dearpygui as dpg
import json
import sys

sys.path.insert(0, "src/world/")
from dialogues import dialogues_callback
from global_variables import global_variables_callback
from player_types import player_types_callback
from shops import shops_callback


def world_callback():
    with dpg.window(label="World", tag="world_window"):
        dpg.add_button(label="Player Types", callback=player_types_callback)
        dpg.add_button(label="Dialogues", callback=dialogues_callback)
        dpg.add_button(label="Shops", callback=shops_callback)
        dpg.add_button(label="Global Variables", callback=global_variables_callback)
