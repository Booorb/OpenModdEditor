import dearpygui.dearpygui as dpg
import json
import webbrowser
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

def script_editor_callback():
    with dpg.window(label="Scripts", tag="scripts_window"):
        dpg.add_button(label="Global Scripts", callback=global_scripts_callback)
