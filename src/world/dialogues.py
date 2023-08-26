import dearpygui.dearpygui as dpg
import json


def new_option_callback():
    if dpg.does_item_exist("new_option_window"):
        dpg.show_item("new_option_window")
    else:
        with dpg.window(label="New Option", tag="new_option_window"):
            with open(gameFolder + "/taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_text("Name:")
                dpg.add_input_text(tag="new_option_name")
                dpg.add_text("Run script:")
                script_list = []
                if "scripts" in data["data"].keys():
                    for script in data["data"]["scripts"]:
                        script_list.append(script)
                    dpg.add_combo(
                        items=script_list,
                        tag="select_script_button",
                    )
                else:
                    dpg.add_text("no scripts exist, please create a script first!")
                dpg.add_text("Follow-Up Dialogue:")
                dialogue_list = []
                if "dialogues" in data["data"].keys():
                    for dialogue in data["data"]["dialogues"]:
                        dialogue_list.append(dialogue)
                    dpg.add_combo(
                        items=dialogue_list,
                        tag="select_follow_up_dialogue_button",
                    )
                else:
                    dpg.add_text("no dialogues exist, please create a dialogue first!")


def edit_option_callback():
    if dpg.does_item_exist("edit_option_window"):
        dpg.show_item("edit_option_window")
    else:
        with dpg.window(label="Edit Option", tag="edit_option_window"):
            with open(gameFolder + "/taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_text("Name:")
                if (
                    "name"
                    in data["data"]["dialogues"][
                        dpg.get_value("select_dialogue_button")
                    ]["options"][0].keys()
                ):
                    dpg.add_input_text(
                        default_value=data["data"]["dialogues"][
                            dpg.get_value("select_dialogue_button")
                        ]["options"][0]["name"],
                        tag="new_option_name",
                    )
                else:
                    dpg.add_input_text(
                        tag="new_option_name",
                    )
                dpg.add_text("Run script:")
                script_list = []
                if "scripts" in data["data"].keys():
                    for script in data["data"]["scripts"]:
                        script_list.append(script)
                    if (
                        "scriptName"
                        in data["data"]["dialogues"][
                            dpg.get_value("select_dialogue_button")
                        ]["options"][0].keys()
                    ):
                        dpg.add_combo(
                            items=script_list,
                            default_value=data["data"]["dialogues"][
                                dpg.get_value("select_dialogue_button")
                            ]["options"][0]["scriptName"],
                            tag="select_script_button",
                        )
                    else:
                        dpg.add_combo(
                            items=script_list,
                            tag="select_script_button",
                        )
                else:
                    dpg.add_text("no scripts exist, please create a script first!")
                dpg.add_text("Follow-Up Dialogue:")
                dialogue_list = []
                if "dialogues" in data["data"].keys():
                    for dialogue in data["data"]["dialogues"]:
                        dialogue_list.append(dialogue)
                    if (
                        "followUpDialogue"
                        in data["data"]["dialogues"][
                            dpg.get_value("select_dialogue_button")
                        ]["options"][0].keys()
                    ):
                        dpg.add_combo(
                            items=dialogue_list,
                            default_value=data["data"]["dialogues"][
                                dpg.get_value("select_dialogue_button")
                            ]["options"][0]["followUpDialogue"],
                            tag="select_follow_up_dialogue_button",
                        )
                    else:
                        dpg.add_combo(
                            items=dialogue_list,
                            tag="select_follow_up_dialogue_button",
                        )
                else:
                    dpg.add_text("no dialogues exist, please create a dialogue first!")


def new_dialogue_callback():
    if dpg.does_item_exist("update_dialogue_window"):
        dpg.delete_item("update_dialogue_window")
    if dpg.does_item_exist("new_dialogue_window"):
        dpg.show_item("new_dialogue_window")
    else:
        with dpg.window(label="New Dialogue", tag="new_dialogue_window"):
            dpg.add_text("ID:")
            dpg.add_input_text(tag="new_dialogue_id")
            dpg.add_text("Name:")
            dpg.add_input_text(tag="new_dialogue_name")
            dpg.add_text("Title:")
            dpg.add_input_text(tag="new_dialogue_title")
            dpg.add_text("HTML Message:")
            dpg.add_input_text(multiline=True, tag="new_dialogue_message")
            dpg.add_text("Image:")
            dpg.add_input_text(tag="new_dialogue_image")
            dpg.add_text("Letter Print Speed:")
            dpg.add_slider_int(tag="new_dialogue_print_speed")
            dpg.add_text("Options:")
            dpg.add_button(label="New Option", callback=new_option_callback)
            dpg.add_button(label="Save", callback=save_callback)


def select_dialogue_callback():
    if dpg.does_item_exist("select_dialogue_window"):
        dpg.show_item("select_dialogue_window")
    else:
        with dpg.window(label="Select Dialogue", tag="select_dialogue_window"):
            with open(gameFolder + "/taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_text("Select Dialogue:")
                dialogue_list = []
                if "dialogues" in data["data"].keys():
                    for dialogue in data["data"]["dialogues"]:
                        dialogue_list.append(dialogue)
                    dpg.add_listbox(
                        items=dialogue_list,
                        tag="select_dialogue_button",
                        callback=update_dialogue_callback,
                    )
                else:
                    dpg.add_text("no dialogues exist, please create a dialogue first!")


def update_dialogue_callback():
    if dpg.does_item_exist("new_dialogue_window"):
        dpg.delete_item("new_dialogue_window")
    elif dpg.does_item_exist("update_dialogue_window"):
        dpg.delete_item("update_dialogue_window")
    dpg.hide_item("select_dialogue_window")
    with open(gameFolder + "/taro2/src/game.json") as f:
        data = json.load(f)
        with dpg.window(label="Update Dialogue", tag="update_dialogue_window"):
            dpg.add_text("ID:")
            dpg.add_input_text(
                default_value=dpg.get_value("select_dialogue_button"),
                tag="new_dialogue_id",
            )
            dpg.add_text("Name:")
            dpg.add_input_text(
                default_value=data["data"]["dialogues"][
                    dpg.get_value("select_dialogue_button")
                ]["name"],
                tag="new_dialogue_name",
            )
            dpg.add_text("Title:")
            dpg.add_input_text(
                default_value=data["data"]["dialogues"][
                    dpg.get_value("select_dialogue_button")
                ]["dialogueTitle"],
                tag="new_dialogue_title",
            )
            dpg.add_text("HTML Message:")
            dpg.add_input_text(
                default_value=data["data"]["dialogues"][
                    dpg.get_value("select_dialogue_button")
                ]["message"],
                multiline=True,
                tag="new_dialogue_message",
            )
            dpg.add_text("Image:")
            dpg.add_input_text(
                default_value=data["data"]["dialogues"][
                    dpg.get_value("select_dialogue_button")
                ]["image"],
                tag="new_dialogue_image",
            )
            dpg.add_text("Letter Print Speed:")
            dpg.add_slider_int(
                default_value=data["data"]["dialogues"][
                    dpg.get_value("select_dialogue_button")
                ]["letterPrintSpeed"],
                tag="new_dialogue_print_speed",
            )
            dpg.add_text("Options:")
            dpg.add_button(label="Edit Option", callback=edit_option_callback)
            dpg.add_button(label="Save", callback=save_callback)


def save_callback():
    with open(gameFolder + "/taro2/src/game.json") as f:
        data = json.load(f)
        if not "dialogues" in data["data"].keys():
            data["data"]["dialogues"] = {}
        data["data"]["dialogues"][dpg.get_value("new_dialogue_id")] = {
            "name": dpg.get_value("new_dialogue_name"),
            "dialogueTitle": dpg.get_value("new_dialogue_title"),
            "message": dpg.get_value("new_dialogue_message"),
            "image": dpg.get_value("new_dialogue_image"),
            "letterPrintSpeed": dpg.get_value("new_dialogue_print_speed"),
            "options": [
                {
                    "name": dpg.get_value("new_option_name"),
                    "scriptName": dpg.get_value("select_script_button"),
                    "followUpDialogue": dpg.get_value(
                        "select_follow_up_dialogue_button"
                    ),
                }
            ],
        }
        json.dump(data, open(gameFolder + "/taro2/src/game.json", "w"), indent=4)
        if dpg.does_item_exist("new_dialogue_window"):
            dpg.delete_item("new_dialogue_window")
        elif dpg.does_item_exist("update_dialogue_window"):
            dpg.delete_item("update_dialogue_window")


def dialogues_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        global gameFolder
        gameFolder = settings["gameFolder"]
    if dpg.does_item_exist("dialogues_window"):
        dpg.show_item("dialogues_window")
    else:
        with dpg.window(label="Dialogoues", tag="dialogues_window"):
            dpg.add_button(label="New Dialogue", callback=new_dialogue_callback)
            dpg.add_button(label="Update Dialogue", callback=select_dialogue_callback)
