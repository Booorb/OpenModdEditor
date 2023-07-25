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
from setup import import_game_file_callback
from settings import fullscreen_callback
from settings import edit_callback
from settings import save_callback
from update import update_project_callback

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.font_registry():
    with open("storage.json") as f:
        data = json.load(f)
        data["editorFolder"] = os.getcwd()
        json.dump(data, open("storage.json", "w"), indent=4)
        default_font = dpg.add_font(
            data["editorFolder"] + "/assets/OpenSans-Regular.ttf", 20
        )


def open_callback(sender, app_data):
    with open(editorFolder + "/storage.json") as f:
        data = json.load(f)
        data["gameFolder"] = app_data["file_path_name"]
        json.dump(data, open(editorFolder + "/storage.json", "w"), indent=4)
        os.chdir(data["gameFolder"])


def cancel_callback(sender, app_data):
    print("Cancel was clicked.")


dpg.add_file_dialog(
    directory_selector=True,
    show=False,
    callback=open_callback,
    tag="change_folder_selector",
    cancel_callback=cancel_callback,
    width=700,
    height=400,
)


with dpg.file_dialog(
    directory_selector=False,
    show=False,
    callback=import_game_file_callback,
    id="import_game_file",
    width=700,
    height=400,
):
    dpg.add_file_extension(".json", color=(0, 255, 0, 255), custom_text="[JSON]")


def setup_ui():
    os.chdir(data["gameFolder"])
    if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
        dpg.add_text("Update Project:")
        dpg.add_button(
            label="Update",
            tag="update_project_button",
            callback=update_project_callback,
        )
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
            callback=lambda: dpg.show_item("change_folder_selector"),
        )


with dpg.window(label="Menu", tag="default_window"):
    dpg.set_primary_window("default_window", True)
    dpg.bind_font(default_font)
    with open("storage.json") as f:
        data = json.load(f)
        global editorFolder
        editorFolder = data["editorFolder"]
        if os.path.exists(data["gameFolder"]):
            setup_ui()
        else:
            data["gameFolder"] = os.getcwd()
            json.dump(data, open("storage.json", "w"), indent=4)
            setup_ui()

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(
            dpg.mvThemeCol_Text, (219, 251, 249, 255), category=dpg.mvThemeCat_Core
        )
        dpg.add_theme_color(
            dpg.mvThemeCol_FrameBg, (69, 89, 92, 255), category=dpg.mvThemeCat_Core
        )
        dpg.add_theme_color(
            dpg.mvThemeCol_CheckMark, (119, 244, 216, 153), category=dpg.mvThemeCat_Core
        )
        dpg.add_theme_color(
            dpg.mvThemeCol_WindowBg, (38, 39, 44, 255), category=dpg.mvThemeCat_Core
        )
        dpg.add_theme_style(
            dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core
        )
        dpg.add_theme_style(
            dpg.mvStyleVar_WindowRounding, 8, category=dpg.mvThemeCat_Core
        )

dpg.bind_theme(global_theme)

dpg.create_viewport(title="OpenModdEditor", width=800, height=600)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
