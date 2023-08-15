import dearpygui.dearpygui as dpg
import json
import webbrowser
import os
from re import sub


def snake_case(s):
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


with open("settings.json") as f:
    data = json.load(f)
    editorFolder = data["editorFolder"]

    def global_scripts_callback():
        with open(editorFolder + "/settings.json") as f:
            data = json.load(f)
            with open(data["gameFolder"] + "/taro2/src/game.json") as f:
                game = json.load(f)
                webbrowser.open(
                    data["gameFolder"] + "/" + snake_case(game["title"]) + "/scripts.py"
                )

    def entity_scripts_callback():
        with open(editorFolder + "/settings.json") as f:
            data = json.load(f)
            with open(data["gameFolder"] + "/taro2/src/game.json") as f:
                game = json.load(f)
                webbrowser.open(
                    data["gameFolder"]
                    + "/"
                    + snake_case(game["title"])
                    + "/entity_scripts.py"
                )

    def compile_scripts_callback():
        with open(editorFolder + "/settings.json") as f:
            data = json.load(f)
            with open(data["gameFolder"] + "/taro2/src/game.json") as f:
                game = json.load(f)
                os.system(
                    "cd "
                    + data["gameFolder"]
                    + "/"
                    + snake_case(game["title"])
                    + " && pymodd compile"
                )


def script_editor_callback():
    with dpg.window(label="Scripts", tag="scripts_window"):
        dpg.add_button(label="Global Scripts", callback=global_scripts_callback)
        dpg.add_button(label="Entity Scripts", callback=entity_scripts_callback)
        dpg.add_button(label="Compile Scripts", callback=compile_scripts_callback)
