import dearpygui.dearpygui as dpg
import json
import webbrowser
import os
import shutil
from re import sub


def snake_case(s):
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


with open("settings.json") as f:
    data = json.load(f)
    if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
        with open(data["gameFolder"] + "/taro2/src/game.json") as f:
            game = json.load(f)

            def global_scripts_callback():
                webbrowser.open(
                    data["gameFolder"] + "/" + snake_case(game["title"]) + "/scripts.py"
                )

            def entity_scripts_callback():
                webbrowser.open(
                    data["gameFolder"]
                    + "/"
                    + snake_case(game["title"])
                    + "/entity_scripts.py"
                )

            def compile_scripts_callback():
                os.system(
                    "cd "
                    + data["gameFolder"]
                    + "/"
                    + snake_case(game["title"])
                    + " && pymodd compile"
                )
                json_names = [
                    filename
                    for filename in os.listdir(
                        data["gameFolder"] + "/" + snake_case(game["title"] + "/output")
                    )
                    if filename.endswith(".json")
                ]

                for json_name in json_names:
                    shutil.copyfile(
                        data["gameFolder"]
                        + "/"
                        + snake_case(game["title"])
                        + "/output/"
                        + json_name,
                        data["gameFolder"] + "/taro2/src/game.json",
                    )


def script_editor_callback():
    if dpg.does_item_exist("scripts_window"):
        dpg.show_item("scripts_window")
    else:
        with dpg.window(label="Scripts", tag="scripts_window"):
            if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
                dpg.add_button(label="Global Scripts", callback=global_scripts_callback)
                dpg.add_button(label="Entity Scripts", callback=entity_scripts_callback)
                dpg.add_button(
                    label="Compile Scripts", callback=compile_scripts_callback
                )
            else:
                dpg.add_text("Please setup a project first!")
