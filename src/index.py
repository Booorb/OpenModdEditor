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
    default_font = dpg.add_font("OpenSans-Regular.ttf", 20)


def open_callback(sender, app_data):
    print("Sender: ", sender)
    print("App Data: ", app_data["file_path_name"])
    with open("storage.json") as f:
        data = json.load(f)
        data["folder"] = app_data["file_path_name"]
        json.dump(data, open("storage.json", "w"), indent=4)
        shutil.copyfile("storage.json", data["folder"] + "/storage.json")
        shutil.copyfile(
            "OpenSans-Regular.ttf", data["folder"] + "/OpenSans-Regular.ttf"
        )
        shutil.copytree("templates", data["folder"] + "/templates", dirs_exist_ok=True)
        os.chdir(data["folder"])


dpg.add_file_dialog(
    directory_selector=True,
    show=False,
    callback=open_callback,
    tag="file_dialog_id",
    width=700,
    height=400,
)

with dpg.window(label="Menu", tag="default_window"):
    with open("storage.json") as f:
        data = json.load(f)
        shutil.copyfile("storage.json", data["folder"] + "/storage.json")
        shutil.copyfile(
            "OpenSans-Regular.ttf", data["folder"] + "/OpenSans-Regular.ttf"
        )
        shutil.copytree("templates", data["folder"] + "/templates", dirs_exist_ok=True)
        os.chdir(data["folder"])
    dpg.set_primary_window("default_window", True)
    dpg.bind_font(default_font)
    if os.path.isfile("taro2/src/game.json"):
        dpg.add_text("Change Project:")
        dpg.add_button(
            label="Change",
            tag="setup_open_button",
            callback=lambda: dpg.show_item("file_dialog_id"),
        )
        dpg.add_text("Update Project:")
        dpg.add_button(label="Update", callback=setup_project_callback)
        dpg.add_text("Edit Game Settings:")
        dpg.add_button(label="Edit", callback=edit_callback)
        dpg.add_text("Play the game:")
        dpg.add_button(label="Play", callback=play_callback)
    else:
        dpg.add_text("Create Project:", tag="setup_project_text")
        dpg.add_button(
            label="Create", tag="setup_project_button", callback=setup_project_callback
        )
        dpg.add_text("Change Project:")
        dpg.add_button(
            label="Change",
            tag="setup_open_button",
            callback=lambda: dpg.show_item("file_dialog_id"),
        )


dpg.create_viewport(title="OpenGameBuilder", width=800, height=600)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
