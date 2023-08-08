import dearpygui.dearpygui as dpg


def global_variables_callback():
    with dpg.window(label="Global Variables", tag="global_variables_window"):
        dpg.add_text("lorem ipsum")
