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
    os.chdir(data["gameFolder"])
    os.system("git clone https://github.com/moddio/taro2.git")
    filereplace("taro2/server/server.js", "80", "3000")
    os.system("cd taro2 && npm install")


def save_project():
    with open("taro2/src/game.json") as f:
        game = json.load(f)
        project = {game["title"]: data["gameFolder"]}
        data["projects"].update(project)
        json.dump(data, open(data["editorFolder"] + "/settings.json", "w"), indent=4)
        os.system("pymodd generate-project taro2/src/game.json")
        os.chdir(data["editorFolder"])


def packages_callback():
    dpg.delete_item("packages_button")
    dpg.set_value(value="Started downloading npm packages...", item="packages_text")
    os.system("cd taro2 && npm install")
    dpg.set_value(value="Finished downloading npm packages...", item="packages_text")


def continue_anyway_callback():
    dpg.configure_item("game_exists_popup", show=False)


def setup_project_callback():
    if dpg.does_item_exist("setup_project_window"):
        dpg.show_item("setup_project_window")
    else:
        with dpg.window(label="Setup Manager", tag="setup_project_window"):
            if os.path.isfile(data["gameFolder"] + "/taro2/src/game.json"):
                with dpg.window(
                    modal=True,
                    show=True,
                    tag="game_exists_popup",
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
                        label="Continue anyway", callback=continue_anyway_callback
                    )

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
            dpg.add_button(label="Racer", tag="racer_button", callback=racer_callback)
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
        save_project()

    def blank_template_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/BlankTemplate.json",
            "taro2/src/game.json",
        )
        save_project()

    def cell_eater_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/CellEater.json", "taro2/src/game.json"
        )
        save_project()

    def deathmatch_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Deathmatch.json", "taro2/src/game.json"
        )
        save_project()

    def guided_tutorial_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/GuidedTutorial.json",
            "taro2/src/game.json",
        )
        save_project()

    def hunt_and_gather_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/HuntAndGather.json",
            "taro2/src/game.json",
        )
        save_project()

    def platformer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Platformer.json", "taro2/src/game.json"
        )
        save_project()

    def racer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Racer.json", "taro2/src/game.json"
        )
        save_project()

    def soccer_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/Soccer.json", "taro2/src/game.json"
        )
        save_project()

    def team_elimination_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/TeamElimination.json",
            "taro2/src/game.json",
        )
        save_project()

    def tower_defense_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/TowerDefense.json", "taro2/src/game.json"
        )
        save_project()

    def zombie_tag_callback():
        game_callback()
        shutil.copyfile(
            data["editorFolder"] + "/templates/ZombieTag.json", "taro2/src/game.json"
        )
        save_project()

    def import_game_file_callback(sender, app_data, user_data):
        game_callback()
        shutil.copyfile(app_data["file_path_name"], "taro2/src/game.json")
        save_project()


def game_callback():
    if dpg.does_item_exist("please_wait_popup"):
        dpg.configure_item("please_wait_popup", show=True)
    taro2_callback()
    if dpg.does_item_exist("please_wait_popup"):
        dpg.configure_item("please_wait_popup", show=False)
    if dpg.does_item_exist("setup_project_window"):
        dpg.configure_item("setup_project_window", show=False)
    if dpg.does_item_exist("project_manager_window"):
        dpg.configure_item("project_manager_window", show=False)
