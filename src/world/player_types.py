import dearpygui.dearpygui as dpg
import json
import matplotlib
import numpy


def new_player_type_callback():
    if dpg.does_item_exist("new_player_type_window"):
        dpg.show_item("new_player_type_window")
    else:
        with dpg.window(
            label="New Player Type", tag="new_player_type_window", width=250
        ):
            dpg.add_text("ID:")
            dpg.add_input_text(tag="player_type_id")
            dpg.add_text("Name:")
            dpg.add_input_text(tag="player_types_name")
            dpg.add_text("Color:")
            dpg.add_color_edit(tag="player_types_color")
            dpg.add_text("Show name label:")
            dpg.add_checkbox(tag="player_types_label")
            with open(gameFolder + "/taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_text("Variables:")
                variables_list = []
                if "entityTypeVariables" in data["data"].keys():
                    for variable in data["data"]["entityTypeVariables"]:
                        variables_list.append(variable)
                    dpg.add_combo(
                        items=variables_list,
                        tag="select_variable_button",
                    )
                dpg.add_text("Diplomacy")
                dpg.add_separator()
                player_types_list = []
                if "playerTypes" in data["data"].keys():
                    for player_type in data["data"]["playerTypes"]:
                        player_types_list.append(player_type)
                        dpg.add_text(player_type + ":")
                        dpg.add_combo(
                            default_value="neutral",
                            items=["neutral", "friendly", "hostile"],
                            tag=player_type + "_diplomacy_button",
                        )
            dpg.add_button(label="Save", callback=save_callback)


def save_callback():
    with open(gameFolder + "/taro2/src/game.json") as f:
        data = json.load(f)
        playerTypesColor255Range = list(map(int, dpg.get_value("player_types_color")))
        playerTypesColor1Range = numpy.divide(playerTypesColor255Range, 255)
        playerTypesColorHex = matplotlib.colors.to_hex(playerTypesColor1Range)
        data["data"]["playerTypes"][dpg.get_value("player_type_id")] = {
            "name": dpg.get_value("player_types_name"),
            "color": playerTypesColorHex,
            "showNameLabel": dpg.get_value("player_types_label"),
            "relationships": {},
        }
        if (
            dpg.get_value("select_variable_button")
            in data["data"]["entityTypeVariables"].keys()
        ):
            data["data"]["playerTypes"][dpg.get_value("player_type_id")][
                "variables"
            ] = {
                dpg.get_value("select_variable_button"): data["data"][
                    "entityTypeVariables"
                ][dpg.get_value("select_variable_button")]
            }
            playerTypeVariables = {
                dpg.get_value("select_variable_button"): data["data"][
                    "entityTypeVariables"
                ][dpg.get_value("select_variable_button")]
            }
            data["data"]["playerTypeVariables"].update(playerTypeVariables)
        if "playerTypes" in data["data"].keys():
            for player_type in data["data"]["playerTypes"]:
                relationship = {
                    player_type: dpg.get_value(player_type + "_diplomacy_button")
                }

                data["data"]["playerTypes"][dpg.get_value("player_type_id")][
                    "relationships"
                ].update(relationship)

        json.dump(data, open(gameFolder + "/taro2/src/game.json", "w"), indent=4)
        with open("settings.json") as f:
            settings = json.load(f)
            settings["projects"][data["title"]][dpg.get_value("player_type_id")] = {
                "playerTypesColor": [dpg.get_value("player_types_color")]
            }
            json.dump(settings, open("settings.json", "w"), indent=4)
        if dpg.does_item_exist("new_player_type_window"):
            dpg.delete_item("new_player_type_window")


def player_types_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        global gameFolder
        gameFolder = settings["gameFolder"]
    if dpg.does_item_exist("player_types_window"):
        dpg.show_item("player_types_window")
    else:
        with dpg.window(label="Player Types", tag="player_types_window"):
            dpg.add_button(label="New Player Type", callback=new_player_type_callback)
