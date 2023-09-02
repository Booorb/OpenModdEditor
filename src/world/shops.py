import dearpygui.dearpygui as dpg
import json


def shops_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        global gameFolder
        gameFolder = settings["gameFolder"]
    if dpg.does_item_exist("shops_window"):
        dpg.show_item("shops_window")
    else:
        with dpg.window(label="Shops", tag="shops_window"):
            dpg.add_text("ID:")
            dpg.add_input_text(tag="shop_id")
            dpg.add_text("Name:")
            dpg.add_input_text(tag="shop_name")
            dpg.add_text("Description:")
            dpg.add_input_text(tag="shop_description")
            dpg.add_text("Dismissible:")
            dpg.add_checkbox(tag="dismiss_shop")
            dpg.add_button(label="Save", callback=save_callback)


def save_callback():
    with open(gameFolder + "/taro2/src/game.json") as f:
        data = json.load(f)
        data["data"]["shops"][dpg.get_value("shop_id")] = {
            "name": dpg.get_value("shop_name"),
            "description": dpg.get_value("shop_description"),
            "dismissible": dpg.get_value("dismiss_shop"),
        }
        json.dump(data, open(gameFolder + "/taro2/src/game.json", "w"), indent=4)
        if dpg.does_item_exist("shops_window"):
            dpg.delete_item("shops_window")
