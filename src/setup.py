import dearpygui.dearpygui as dpg
from pyutil import filereplace
import webbrowser
import os
import shutil
import json
from settings import edit_callback
from update import update_project_callback


def play_callback():
    os.system("cd taro2 && npm run server&")
    webbrowser.open("http://localhost:3000/", new=2)


def taro2_callback():
    dpg.delete_item("taro2_button")
    dpg.set_value(value="Started downloading taro2...", item="taro2_text")
    os.system("git clone https://github.com/moddio/taro2.git")
    filereplace("taro2/server/server.js", "80", "3000")
    dpg.set_value(value="Finished downloading taro2...", item="taro2_text")


def packages_callback():
    dpg.delete_item("packages_button")
    dpg.set_value(value="Started downloading npm packages...", item="packages_text")
    os.system("cd taro2 && npm install")
    dpg.set_value(value="Finished downloading npm packages...", item="packages_text")


def setup_project_callback():
    if dpg.does_item_exist("setup_project"):
        dpg.show_item("setup_project")
    else:
        with dpg.window(label="Setup Manager", tag="setup_project"):
            if os.path.isdir("taro2"):
                dpg.add_text("Taro2 is already installed!")
            else:
                dpg.add_text("Download Taro2:", tag="taro2_text")
                dpg.add_button(
                    label="Download", tag="taro2_button", callback=taro2_callback
                )

            if os.path.isdir("taro2/node_modules"):
                dpg.add_text("Already installed npm packages!")
            else:
                dpg.add_text("Download npm packages:", tag="packages_text")
                dpg.add_button(
                    label="Download",
                    tag="packages_button",
                    callback=packages_callback,
                )
            if os.path.isfile("taro2/src/game.json"):
                dpg.add_text("Already added game.json!")
            else:
                dpg.add_text("Download template game or upload own game.json file:")
                dpg.add_button(
                    label="Battle Royale",
                    tag="battle_royale_button",
                    callback=battle_royale_callback,
                )
                dpg.add_button(
                    label="Blank Template",
                    tag="blank_template_button",
                    callback=blank_template_callback,
                )
                dpg.add_button(
                    label="Cell Eater",
                    tag="cell_eater_button",
                    callback=cell_eater_callback,
                )
                dpg.add_button(
                    label="Deathmatch",
                    tag="deathmatch_button",
                    callback=deathmatch_callback,
                )
                dpg.add_button(
                    label="Guided Tutorial",
                    tag="guided_tutorial_button",
                    callback=guided_tutorial_callback,
                )
                dpg.add_button(
                    label="Hunt and Gather",
                    tag="hunt_and_gather_button",
                    callback=hunt_and_gather_callback,
                )
                dpg.add_button(
                    label="Platformer",
                    tag="platformer_button",
                    callback=platformer_callback,
                )
                dpg.add_button(
                    label="Racer", tag="racer_button", callback=racer_callback
                )
                dpg.add_button(
                    label="Soccer", tag="soccer_button", callback=soccer_callback
                )
                dpg.add_button(
                    label="Team Elimination",
                    tag="team_elimination_button",
                    callback=team_elimination_callback,
                )
                dpg.add_button(
                    label="Tower Defense",
                    tag="tower_defense_button",
                    callback=tower_defense_callback,
                )
                dpg.add_button(
                    label="Zombie Tag",
                    tag="zombie_tag_button",
                    callback=zombie_tag_callback,
                )


with open("storage.json") as f:
    data = json.load(f)

    def battle_royale_callback():
        shutil.copyfile(
            data["editor"] + "/templates/BattleRoyale.json", "taro2/src/game.json"
        )
        game_callback()

    def blank_template_callback():
        shutil.copyfile(
            data["editor"] + "/templates/BlankTemplate.json", "taro2/src/game.json"
        )
        game_callback()

    def cell_eater_callback():
        shutil.copyfile(
            data["editor"] + "/templates/CellEater.json", "taro2/src/game.json"
        )
        game_callback()

    def deathmatch_callback():
        shutil.copyfile(
            data["editor"] + "/templates/Deathmatch.json", "taro2/src/game.json"
        )
        game_callback()

    def guided_tutorial_callback():
        shutil.copyfile(
            data["editor"] + "/templates/GuidedTutorial.json", "taro2/src/game.json"
        )
        game_callback()

    def hunt_and_gather_callback():
        shutil.copyfile(
            data["editor"] + "/templates/HuntAndGather.json", "taro2/src/game.json"
        )
        game_callback()

    def platformer_callback():
        shutil.copyfile(
            data["editor"] + "/templates/Platformer.json", "taro2/src/game.json"
        )
        game_callback()

    def racer_callback():
        shutil.copyfile(data["editor"] + "/templates/Racer.json", "taro2/src/game.json")
        game_callback()

    def soccer_callback():
        shutil.copyfile(
            data["editor"] + "/templates/Soccer.json", "taro2/src/game.json"
        )
        game_callback()

    def team_elimination_callback():
        shutil.copyfile(
            data["editor"] + "/templates/TeamElimination.json", "taro2/src/game.json"
        )
        game_callback()

    def tower_defense_callback():
        shutil.copyfile(
            data["editor"] + "/templates/TowerDefense.json", "taro2/src/game.json"
        )
        game_callback()

    def zombie_tag_callback():
        shutil.copyfile(
            data["editor"] + "/templates/ZombieTag.json", "taro2/src/game.json"
        )
        game_callback()


def game_callback():
    dpg.hide_item("setup_project")
    dpg.delete_item("setup_project_text")
    dpg.delete_item("setup_project_button")
    dpg.delete_item("setup_change_folder_text")
    dpg.delete_item("setup_change_folder_button")
    if dpg.does_item_exist("update_project_button"):
        print("button exists")
    else:
        dpg.add_text("Update Project:", parent="default_window")
        dpg.add_button(
            label="Update",
            parent="default_window",
            tag="update_project_button",
            callback=update_project_callback,
        )
        dpg.add_text("Edit Game Settings:", parent="default_window")
        dpg.add_button(label="Edit", parent="default_window", callback=edit_callback)
        dpg.add_text("Play the game:", parent="default_window")
        dpg.add_button(label="Play", parent="default_window", callback=play_callback)
