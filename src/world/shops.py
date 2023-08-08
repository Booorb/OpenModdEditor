import dearpygui.dearpygui as dpg


def shops_callback():
    with dpg.window(label="Shops", tag="shops_window"):
        dpg.add_text("lorem ipsum")
