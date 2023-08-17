import dearpygui.dearpygui as dpg
import json
import matplotlib
import numpy


def new_player_type_callback():
    if dpg.does_item_exist("new_player_type_window"):
        dpg.show_item("new_player_type_window")
    else:
        with dpg.window(
            label="New Player Type", tag="new_player_type_window", width=250
        ):
            dpg.add_text("ID:")
            dpg.add_input_text(tag="player_type_id")
            dpg.add_text("Name:")
            dpg.add_input_text(tag="player_types_name")
            dpg.add_text("Color:")
            dpg.add_color_edit(tag="player_types_color")
            dpg.add_text("Show name label:")
            dpg.add_checkbox(tag="player_types_label")
            dpg.add_button(label="Save", callback=save_callback)


def save_callback():
    with open("taro2/src/game.json") as f:
        data = json.load(f)
        playerTypesColor255Range = list(map(int, dpg.get_value("player_types_color")))
        playerTypesColor1Range = numpy.divide(playerTypesColor255Range, 255)
        playerTypesColorHex = matplotlib.colors.to_hex(playerTypesColor1Range)
        data["data"]["playerTypes"][dpg.get_value("player_type_id")] = {
            "name": dpg.get_value("player_types_name"),
            "color": playerTypesColorHex,
            "showNameLabel": dpg.get_value("player_types_label"),
        }
        json.dump(data, open("taro2/src/game.json", "w"), indent=4)


def player_types_callback():
    if dpg.does_item_exist("player_types_window"):
        dpg.show_item("player_types_window")
    else:
        with dpg.window(label="Player Types", tag="player_types_window"):
            dpg.add_button(label="New Player Type", callback=new_player_type_callback)
