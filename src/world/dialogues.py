import dearpygui.dearpygui as dpg
import json


def new_dialogue_callback():
    with dpg.window(label="New Dialogue", tag="new_dialogue_window", width=400):
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
        dpg.add_button(label="Save", callback=save_callback)
    if dpg.does_item_exist("new_dialogue_window"):
        dpg.show_item("new_dialogue_window")
    else:
        with dpg.window(label="New Dialogue", tag="new_dialogue_window", width=400):
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
            dpg.add_button(label="Save", callback=save_callback)


def select_dialogue_callback():
    if dpg.does_item_exist("select_dialogue_window"):
        dpg.show_item("select_dialogue_window")
    else:
        with dpg.window(label="Select Dialogue", tag="select_dialogue_window"):
            with open("taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_text("Select Dialogue:")
                dialogue_list = []
                if "dialogues" in data["data"].keys():
                    for dialogue in data["data"]["dialogues"]:
                        dialogue_list.append(dialogue)
                    dpg.add_combo(
                        items=dialogue_list,
                        tag="select_dialogue_button",
                    )
                else:
                    dpg.add_text("no dialogues exist, please create a dialogue first!")
def save_callback(sender):
    with open("taro2/src/game.json") as f:
        data = json.load(f)
        data["data"]["dialogues"][dpg.get_value("new_dialogue_id")] = {
            "name": dpg.get_value("new_dialogue_name"),
            "dialogueTitle": dpg.get_value("new_dialogue_title"),
            "message": dpg.get_value("new_dialogue_value"),
            "image": dpg.get_value("new_dialogue_image"),
            "letterPrintSpeed": dpg.get_value("new_dialogue_print_speed"),
        }
        json.dump(data, open("taro2/src/game.json", "w"), indent=4)


def dialogues_callback():
    if dpg.does_item_exist("dialogues_window"):
        dpg.show_item("dialogues_window")
    else:
        with dpg.window(label="Dialogoues", tag="dialogues_window"):
            with open("taro2/src/game.json") as f:
                data = json.load(f)
                dpg.add_button(label="New Dialogue", callback=new_dialogue_callback)
                dpg.add_button(
                    label="Update Dialogue", callback=select_dialogue_callback
                )
                dpg.add_separator()
                if "dialogues" in data["data"].keys():
                    for dialogues in data["data"]["dialogues"]:
                        dpg.add_button(
                            label=data["data"]["dialogues"][dialogues]["name"]
                        )
