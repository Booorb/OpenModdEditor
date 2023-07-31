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
    os.system("git clone https://github.com/moddio/taro2.git")
    filereplace("taro2/server/server.js", "80", "3000")
    os.system("cd taro2 && npm install")


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
            if os.path.isfile("taro2/src/game.json"):
                dpg.add_text("Already added game.json!")
            else:
                dpg.add_text("Download template game or import own game.json file:")
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
                dpg.add_separator()
                dpg.add_button(
                    label="Import game.json",
                    tag="import_game_button",
                    callback=lambda: dpg.show_item("import_game_file"),
                )

                with dpg.window(
                    modal=True,
                    show=False,
                    tag="please_wait_popup",
                    no_title_bar=True,
                ):
                    dpg.add_text("Setting up project...")
                    dpg.add_text("Please wait!")


with open("settings.json") as f:
    data = json.load(f)

    def battle_royale_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/BattleRoyale.json", "taro2/src/game.json"
        )

    def blank_template_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/BlankTemplate.json",
            "taro2/src/game.json",
        )

    def cell_eater_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/CellEater.json", "taro2/src/game.json"
        )

    def deathmatch_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Deathmatch.json", "taro2/src/game.json"
        )

    def guided_tutorial_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/GuidedTutorial.json",
            "taro2/src/game.json",
        )

    def hunt_and_gather_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/HuntAndGather.json",
            "taro2/src/game.json",
        )

    def platformer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Platformer.json", "taro2/src/game.json"
        )

    def racer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Racer.json", "taro2/src/game.json"
        )

    def soccer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Soccer.json", "taro2/src/game.json"
        )

    def team_elimination_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/TeamElimination.json",
            "taro2/src/game.json",
        )

    def tower_defense_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/TowerDefense.json", "taro2/src/game.json"
        )

    def zombie_tag_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/ZombieTag.json", "taro2/src/game.json"
        )

    def import_game_file_callback(sender, app_data, user_data):
        game_callback()
        shutil.copyfile(app_data["file_path_name"], "taro2/src/game.json")


def game_callback():
    dpg.configure_item("please_wait_popup", show=True)
    taro2_callback()
    dpg.configure_item("please_wait_popup", show=False)
