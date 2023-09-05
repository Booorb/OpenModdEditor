import dearpygui.dearpygui as dpg
import json
import os


def new_shop_callback():
    if dpg.does_item_exist("update_shop_window"):
        dpg.delete_item("update_shop_window")
    if dpg.does_item_exist("new_shop_window"):
        dpg.show_item("new_shop_window")
    else:
        with dpg.window(label="Shops", tag="new_shop_window"):
            dpg.add_text("ID:")
            dpg.add_input_text(tag="shop_id")
            dpg.add_text("Name:")
            dpg.add_input_text(tag="shop_name")
            dpg.add_text("Description:")
            dpg.add_input_text(tag="shop_description")
            dpg.add_text("Dismissible:")
            dpg.add_checkbox(tag="dismiss_shop")
            dpg.add_button(label="Save", callback=save_callback)


def update_shop_callback():
    if dpg.does_item_exist("new_shop_window"):
        dpg.delete_item("new_shop_window")
    if dpg.does_item_exist("update_shop_window"):
        dpg.delete_item("update_shop_window")
    with open(gameFolder + "/taro2/src/game.json") as f:
        data = json.load(f)
        with dpg.window(label="Shops", tag="update_shop_window"):
            dpg.add_text("ID:")
            dpg.add_input_text(
                default_value=dpg.get_value("select_shop_button"), tag="shop_id"
            )
            dpg.add_text("Name:")
            dpg.add_input_text(
                default_value=data["data"]["shops"][
                    dpg.get_value("select_shop_button")
                ]["name"],
                tag="shop_name",
            )
            dpg.add_text("Description:")
            dpg.add_input_text(
                default_value=data["data"]["shops"][
                    dpg.get_value("select_shop_button")
                ]["description"],
                tag="shop_description",
            )
            dpg.add_text("Dismissible:")
            dpg.add_checkbox(
                default_value=data["data"]["shops"][
                    dpg.get_value("select_shop_button")
                ]["dismissible"],
                tag="dismiss_shop",
            )
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
        if dpg.does_item_exist("new_shop_window"):
            dpg.delete_item("new_shop_window")
        if dpg.does_item_exist("update_shop_window"):
            dpg.delete_item("update_shop_window")


def shops_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        global gameFolder
        gameFolder = settings["gameFolder"]
    if dpg.does_item_exist("shops_window"):
        dpg.show_item("shops_window")
    else:
        with dpg.window(label="Shops", tag="shops_window"):
            if os.path.isfile(gameFolder + "/taro2/src/game.json"):
                dpg.add_button(label="New Shop", callback=new_shop_callback)
                with open(gameFolder + "/taro2/src/game.json") as f:
                    data = json.load(f)
                    dpg.add_text("Update Shop:")
                    shop_list = []
                    if "shops" in data["data"].keys():
                        for shop in data["data"]["shops"]:
                            shop_list.append(shop)
                        dpg.add_listbox(
                            items=shop_list,
                            tag="select_shop_button",
                            callback=update_shop_callback,
                        )
                    else:
                        dpg.add_text("no shops exist, please create a shop first!")
            else:
                dpg.add_text("no project exist, please create a project first!")
