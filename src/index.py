import dearpygui.dearpygui as dpg
import os
import webbrowser
import json
import shutil
from setup import setup_project_callback
from setup import taro2_callback
from setup import game_callback
from setup import import_game_file_callback
from settings import fullscreen_callback
from settings import edit_callback
from settings import import_map_callback
from update import update_project_callback
from about import about_callback
from world import world_callback
from scripts import script_editor_callback
from play import play_callback
import sys

sys.path.insert(0, "src/plugins/")
from ChooseFontsPlugin import ChooseFontsPlugin
from EditThemePlugin import EditThemePlugin

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


def change_folder_callback(sender, app_data):
    with open(editorFolder + "/settings.json") as f:
        data = json.load(f)
        data["gameFolder"] = app_data["file_path_name"]
        json.dump(data, open(editorFolder + "/settings.json", "w"), indent=4)


def cancel_callback(sender, app_data):
    print("Cancel was clicked.")


def project_manager_callback():
    dpg.show_item("project_manager_window")


def discord_callback():
    webbrowser.open("https://discord.gg/uBqVVFcJpz")


def report_bug_callback():
    webbrowser.open("https://codeberg.org/Boorb/OpenModdEditor/issues")


def online_documentation_callback():
    webbrowser.open("https://codeberg.org/Boorb/OpenModdEditor/wiki")


def folder_exists_callback():
    if dpg.does_item_exist("game_exists_popup2"):
        dpg.show_item("game_exists_popup2")
    else:
        if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
            with dpg.window(
                modal=True,
                show=True,
                tag="game_exists_popup2",
                no_title_bar=True,
            ):
                dpg.add_text(
                    "Already added game.json! \nIf you continue, the existing game will be overwritten."
                )
                dpg.add_separator()
                dpg.add_button(
                    label="Change folder",
                    callback=lambda: dpg.show_item("change_folder_selector"),
                )
                dpg.add_button(
                    label="Continue anyway",
                    callback=lambda: dpg.show_item("import_game_file")
                    and dpg.configure_item("please_wait_popup", show=False),
                )
        else:
            dpg.show_item("import_game_file")


def open_project_callback():
    with open(editorFolder + "/settings.json") as f:
        data = json.load(f)
        data["gameFolder"] = data["projects"][dpg.get_value("projects_listbox")][
            "folder"
        ]
        json.dump(data, open(editorFolder + "/settings.json", "w"), indent=4)
        dpg.hide_item("project_manager_window")


dpg.add_file_dialog(
    directory_selector=True,
    show=False,
    callback=change_folder_callback,
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
    cancel_callback=cancel_callback,
    width=700,
    height=400,
):
    dpg.add_file_extension(".json", color=(0, 255, 0, 255), custom_text="[JSON]")


with dpg.file_dialog(
    directory_selector=False,
    show=False,
    callback=import_map_callback,
    id="import_map",
    cancel_callback=cancel_callback,
    width=700,
    height=400,
):
    dpg.add_file_extension(".json", color=(0, 255, 0, 255), custom_text="[JSON]")


def setup_ui():
    with dpg.window(label="Menu", tag="menu_window"):
        dpg.set_primary_window("menu_window", True)
        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="Import Project",
                    callback=folder_exists_callback,
                )

                dpg.add_menu_item(
                    label="Create Project", callback=setup_project_callback
                )

                dpg.add_menu_item(
                    label="Change Folder",
                    callback=lambda: dpg.show_item("change_folder_selector"),
                )

            with dpg.menu(label="View"):
                EditThemePlugin()
                ChooseFontsPlugin()
                dpg.add_menu_item(
                    label="Toggle Fullscreen", callback=fullscreen_callback
                )
                dpg.add_menu_item(
                    label="Update OpenModdEditor", callback=update_project_callback
                )
                dpg.add_separator()
                dpg.add_menu_item(
                    label="Show Project Manager", callback=project_manager_callback
                )
                dpg.add_menu_item(label="Show Settings Window", callback=edit_callback)
                dpg.add_menu_item(label="Show World Window", callback=world_callback)
                dpg.add_separator()
                dpg.add_menu_item(
                    label="Open Script Editor", callback=script_editor_callback
                )

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="Discord Server", callback=discord_callback)
                dpg.add_menu_item(label="Report a Bug", callback=report_bug_callback)
                dpg.add_menu_item(
                    label="Online Documentation", callback=online_documentation_callback
                )
                dpg.add_separator()
                dpg.add_menu_item(label="About OpenModdEditor", callback=about_callback)

            dpg.add_menu_item(label="Play", callback=play_callback)

    with dpg.group(tag="setup_project_group"):
        projects_title = dpg.add_text("Your Projects:")
        if "projects" in data.keys():
            project_list = []
            for project in data["projects"]:
                if os.path.isfile(
                    data["projects"][project]["folder"] + "/taro2/src/game.json"
                ):
                    project_list.append(project)

            dpg.add_listbox(
                items=project_list,
                tag="projects_listbox",
                callback=open_project_callback,
            )
        else:
            dpg.add_text("no projects yet!")
        dpg.add_separator()
        dpg.add_button(
            label="Create Project",
            callback=setup_project_callback,
        )
        dpg.add_button(
            label="Import Project",
            callback=folder_exists_callback,
        )


with dpg.window(label="Project Manager", tag="project_manager_window"):
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

dpg.create_viewport(title="OpenModdEditor", width=800, height=600)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
