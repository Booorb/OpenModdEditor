import dearpygui.dearpygui as dpg
import os
import json


def start_update_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        os.system("cd " + settings["gameFolder"] + "/taro2 && git pull && npm install")
        os.system("cd " + settings["editorFolder"] + "  && git pull")


def update_project_callback():
    if dpg.does_item_exist("updating_popup"):
        dpg.configure_item("updating_popup", show=True)
    else:
        with dpg.window(
            modal=True,
            show=True,
            tag="updating_popup",
            no_title_bar=True,
        ):
            dpg.add_text("Updating OpenModdEditor...")
            dpg.add_text("Please wait!")
    start_update_callback()
    if dpg.does_item_exist("updating_popup"):
        dpg.configure_item("updating_popup", show=False)
