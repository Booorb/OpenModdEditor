import dearpygui.dearpygui as dpg


def dialogues_callback():
    with dpg.window(label="Dialogoues", tag="dialogues_window"):
        dpg.add_text("lorem ipsum")
