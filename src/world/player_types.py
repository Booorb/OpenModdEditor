import dearpygui.dearpygui as dpg
import json
import matplotlib
import numpy
import os


def new_player_type_callback():
    if dpg.does_item_exist("edit_player_type_window"):
        dpg.delete_item("edit_player_type_window")
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


def update_player_type_callback():
    if dpg.does_item_exist("new_player_type_window"):
        dpg.delete_item("new_player_type_window")
    if dpg.does_item_exist("edit_player_type_window"):
        dpg.delete_item("edit_player_type_window")
    with dpg.window(
        label="Update Player Type", tag="edit_player_type_window", width=250
    ):
        with open(gameFolder + "/taro2/src/game.json") as f:
            data = json.load(f)
            dpg.add_text("ID:")
            dpg.add_input_text(
                default_value=dpg.get_value("select_player_type_button"),
                tag="player_type_id",
            )
            dpg.add_text("Name:")
            dpg.add_input_text(
                default_value=data["data"]["playerTypes"][
                    dpg.get_value("select_player_type_button")
                ]["name"],
                tag="player_types_name",
            )
            dpg.add_text("Color:")
            with open("settings.json") as f:
                settings = json.load(f)
                if (
                    dpg.get_value("player_type_id")
                    in settings["projects"][data["title"]].keys()
                ):
                    dpg.add_color_edit(
                        default_value=settings["projects"][data["title"]][
                            dpg.get_value("player_type_id")
                        ]["playerTypesColor"],
                        tag="player_types_color",
                    )
                else:
                    dpg.add_color_edit(tag="player_types_color")
            dpg.add_text("Show name label:")
            dpg.add_checkbox(
                default_value=data["data"]["playerTypes"][
                    dpg.get_value("select_player_type_button")
                ]["showNameLabel"],
                tag="player_types_label",
            )
            dpg.add_text("Variables:")
            variables_list = []
            if "entityTypeVariables" in data["data"].keys():
                for variable in data["data"]["entityTypeVariables"]:
                    variables_list.append(variable)
                if (
                    "variables"
                    in data["data"]["playerTypes"][
                        dpg.get_value("player_type_id")
                    ].keys()
                ):
                    default_variable = []
                    for variable in data["data"]["playerTypes"][
                        dpg.get_value("player_type_id")
                    ]["variables"].keys():
                        default_variable.append(variable)
                    if default_variable:
                        dpg.add_combo(
                            default_value=default_variable[0],
                            items=variables_list,
                            tag="select_variable_button",
                        )
                    else:
                        dpg.add_combo(
                            items=variables_list,
                            tag="select_variable_button",
                        )
                else:
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
                    if (
                        player_type
                        in data["data"]["playerTypes"][dpg.get_value("player_type_id")][
                            "relationships"
                        ].keys()
                    ):
                        dpg.add_combo(
                            default_value=data["data"]["playerTypes"][
                                dpg.get_value("player_type_id")
                            ]["relationships"][player_type],
                            items=["neutral", "friendly", "hostile"],
                            tag=player_type + "_diplomacy_button",
                        )
                    else:
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
                "playerTypesColor": dpg.get_value("player_types_color")
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
            if os.path.isfile(gameFolder + "/taro2/src/game.json"):
                dpg.add_button(
                    label="New Player Type", callback=new_player_type_callback
                )
                with open(gameFolder + "/taro2/src/game.json") as f:
                    data = json.load(f)
                    dpg.add_text("Update Player Type:")
                    player_type_list = []
                    if "playerTypes" in data["data"].keys():
                        for player_type in data["data"]["playerTypes"]:
                            player_type_list.append(player_type)
                        dpg.add_listbox(
                            items=player_type_list,
                            tag="select_player_type_button",
                            callback=update_player_type_callback,
                        )
                    else:
                        dpg.add_text(
                            "no player types exist, please create a player type first!"
                        )
            else:
                dpg.add_text("no project exist, please create a project first!")
