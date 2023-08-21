import dearpygui.dearpygui as dpg
import webbrowser
import json
import os


def play_callback():
    with open("settings.json") as f:
        data = json.load(f)
        os.system("cd " + data["gameFolder"] + "/taro2 && npm run server&")
        webbrowser.open("http://localhost:3000/", new=2)
