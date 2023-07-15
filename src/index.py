import dearpygui.dearpygui as dpg
import os
import webbrowser
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

with dpg.window(label="Menu", tag="default_window"):
    dpg.set_primary_window("default_window", True)
    if os.path.isfile("taro2/src/game.json"):
        dpg.add_text("Update Project:")
        dpg.add_button(label="Update", callback=setup_project_callback)
        dpg.add_text("Edit Game Settings:")
        dpg.add_button(label="Edit", callback=edit_callback)
        dpg.add_text("Play the game:")
        dpg.add_button(label="Play", callback=play_callback)
    else:
        dpg.add_text("Create Project:", tag="setup_project_text")
        dpg.add_button(label="Create", tag="setup_project_button", callback=setup_project_callback)
        dpg.add_text("Open Project:")
        dpg.add_button(label="Open", tag="setup_open_button")
    

dpg.create_viewport(title='OpenGameBuilder', width=800, height=600)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()