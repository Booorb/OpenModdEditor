import dearpygui.dearpygui as dpg
import os
import webbrowser
import json
import shutil
from setup import setup_project_callback
from setup import taro2_callback
from setup import packages_callback
from setup import game_callback
from setup import play_callback
from settings import fullscreen_callback
from settings import edit_callback
from settings import save_callback

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.font_registry():
    with open("storage.json") as f:
        data = json.load(f)
        data["editor"] = os.getcwd()
        json.dump(data, open("storage.json", "w"), indent=4)
        default_font = dpg.add_font(data["editor"] + "/OpenSans-Regular.ttf", 20)


def open_callback(sender, app_data):
    with open(editor + "/storage.json") as f:
        data = json.load(f)
        data["folder"] = app_data["file_path_name"]
        json.dump(data, open(editor + "/storage.json", "w"), indent=4)
        os.chdir(data["folder"])

def cancel_callback(sender, app_data):
    print('Cancel was clicked.')

dpg.add_file_dialog(
    directory_selector=True,
    show=False,
    callback=open_callback,
    tag="file_dialog_id",
    cancel_callback=cancel_callback,
    width=700,
    height=400,
)


def setup_ui():
    os.chdir(data["folder"])
    if os.path.isfile(data["folder"] + "/taro2/src/game.json"):
        dpg.add_text("Update Project:")
        dpg.add_button(label="Update", callback=setup_project_callback)
        dpg.add_text("Edit Game Settings:")
        dpg.add_button(label="Edit", callback=edit_callback)
        dpg.add_text("Play the game:")
        dpg.add_button(label="Play", callback=play_callback)
    else:
        dpg.add_text("Create Project:", tag="setup_project_text")
        dpg.add_button(
            label="Create",
            tag="setup_project_button",
            callback=setup_project_callback,
        )
        dpg.add_text("Change Folder:", tag="setup_change_folder_text")
        dpg.add_button(
            label="Change",
            tag="setup_change_folder_button",
            callback=lambda: dpg.show_item("file_dialog_id"),
        )


with dpg.window(label="Menu", tag="default_window"):
    dpg.set_primary_window("default_window", True)
    dpg.bind_font(default_font)
    with open("storage.json") as f:
        data = json.load(f)
        global editor
        editor = data["editor"]
        if os.path.exists(data["folder"]):
            setup_ui()
        else:
            data["folder"] = os.getcwd()
            json.dump(data, open("storage.json", "w"), indent=4)
            setup_ui()


dpg.create_viewport(title="OpenGameBuilder", width=800, height=600)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
