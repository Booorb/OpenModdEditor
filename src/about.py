import dearpygui.dearpygui as dpg


def about_callback():
    with dpg.window(label="About", tag="about_project"):
        dpg.add_text(
            "OpenModdEditor is a cross-platform game editor to create 2D multiplayer .io games. \nIt uses Taro2 for the backend, which makes games made with it compatible with modd.io."
        )
