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
from about import about_callback

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.font_registry():
    with open("settings.json") as f:
        data = json.load(f)
        data["editorFolder"] = os.getcwd()
        json.dump(data, open("settings.json", "w"), indent=4)
        default_font = dpg.add_font(
            data["editorFolder"] + "/assets/OpenSans-Regular.ttf", 20
        )
        title_font = dpg.add_font(
            data["editorFolder"] + "/assets/OpenSans-Bold.ttf", 30
        )


def open_callback(sender, app_data):
    with open(editorFolder + "/settings.json") as f:
        data = json.load(f)
        data["gameFolder"] = app_data["file_path_name"]
        json.dump(data, open(editorFolder + "/settings.json", "w"), indent=4)
        os.chdir(data["gameFolder"])


def cancel_callback(sender, app_data):
    print("Cancel was clicked.")


def project_manager_callback():
    dpg.show_item("project_manager_window")


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
    with dpg.window(label="Menu", tag="menu_window"):
        dpg.set_primary_window("menu_window", True)
        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Import Project")
                dpg.add_menu_item(label="Export Project")
                dpg.add_menu_item(
                    label="Open Project",
                )

                with dpg.menu(label="Create Project"):
                    dpg.add_menu_item(label="create project with template")
                    dpg.add_menu_item(label="create empty project")

            with dpg.menu(label="View"):
                dpg.add_menu_item(
                    label="Toggle Fullscreen", callback=fullscreen_callback
                )
                dpg.add_separator()
                dpg.add_menu_item(
                    label="Show Project Manager", callback=fullscreen_callback
                )
                dpg.add_menu_item(
                    label="Show Update Manager", callback=fullscreen_callback
                )
                dpg.add_menu_item(
                    label="Show Settings Window", callback=fullscreen_callback
                )

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="About OpenModdEditor", callback=about_callback)

            dpg.add_menu_item(label="Play")

    with dpg.group(tag="setup_project_group"):
        projects_title = dpg.add_text("Your Projects:")
        if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
            dpg.hide_item("project_manager_window")
            with open("taro2/src/game.json") as f:
                game = json.load(f)
                dpg.add_button(label=game["title"])
        else:
            dpg.add_text("no projects yet!")
        dpg.bind_item_font(projects_title, title_font)
        dpg.add_separator()
        dpg.add_button(
            label="Create Project",
            callback=setup_project_callback,
        )
        dpg.add_button(
            label="Open Project",
            callback=lambda: dpg.show_item("change_folder_selector"),
        )


with dpg.window(label="Project Manager", tag="project_manager_window"):
    dpg.bind_font(default_font)
    with open("settings.json") as f:
        data = json.load(f)
        global editorFolder
        editorFolder = data["editorFolder"]
        if os.path.exists(data["gameFolder"]):
            setup_ui()
        else:
            data["gameFolder"] = os.getcwd()
            json.dump(data, open("settings.json", "w"), indent=4)
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
