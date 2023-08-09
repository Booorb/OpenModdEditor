import dearpygui.dearpygui as dpg
import json


def dialogues_callback():
    with dpg.window(label="Dialogoues", tag="dialogues_window"):
        with open("taro2/src/game.json") as f:
            data = json.load(f)
            dpg.add_button(label="New Dialogue")
            dpg.add_separator()
            if "dialogues" in data["data"].keys():
                for dialogues in data["data"]["dialogues"]:
                    dpg.add_button(label=dialogues)
