import dearpygui.dearpygui as dpg


def player_types_callback():
    with dpg.window(label="Player Types", tag="player_types_window"):
        dpg.add_text("lorem ipsum")
