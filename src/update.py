import dearpygui.dearpygui as dpg
import os


def update_taro2_callback():
    os.system("cd taro2 && git pull")


def update_packages_callback():
    os.system("cd taro2 && npm install")


def update_project_callback():
    if dpg.does_item_exist("update_project"):
        dpg.show_item("update_project")
    else:
        with dpg.window(label="Update Manager", tag="update_project"):
            dpg.add_text("Update Taro2:")
            dpg.add_button(label="Update", callback=update_taro2_callback)
            dpg.add_text("Update npm packages:")
            dpg.add_button(
                label="Update",
                callback=update_packages_callback,
            )
