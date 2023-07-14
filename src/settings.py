import dearpygui.dearpygui as dpg
import json

def edit_callback():
    if dpg.does_item_exist("game_settings"):
        dpg.show_item("game_settings")
    else:
        with dpg.window(label="Settings", tag="game_settings"):
            with dpg.menu_bar():
                with dpg.menu(label="Default"):
                    with open("taro2/src/game.json") as f:
                        data = json.load(f)
                        dpg.add_text("Game Name:")
                        dpg.add_input_text(tag="game_name")
                        dpg.set_value(value=data["title"], item="game_name")
                        dpg.add_text("Game Slug:")
                        dpg.add_input_text(tag="game_slug")
                        dpg.set_value(value=data["gameSlug"], item="game_slug")
                        dpg.add_text("Repository Access:")
                        dpg.add_listbox(items=['Open Source', 'Private'], tag="repository_access")
                        if data["access"] == "private":
                            dpg.set_value(value="Private", item="repository_access")
                        else:
                            dpg.set_value(value="Open Source", item="repository_access")
                        dpg.add_text("Enable video chat:")
                        dpg.add_checkbox(default_value=data["enableVideoChat"], tag="enable_video_chat")
                        dpg.add_text("Hidden:")
                        dpg.add_checkbox(default_value=data["hidden"], tag="hidden")
                        dpg.add_text("Enable Data Saving:")
                        dpg.add_checkbox(default_value=data["enablePersistedData"], tag="enable_persistent_data")
                        dpg.add_text("Enable Context Menu:")
                        dpg.add_checkbox(default_value=data["contextMenuEnabled"], tag="context_menu")
                        dpg.add_text("Daily coin transfer limit:")
                        dpg.add_slider_int(default_value=data["dailyCoinTransferLimit"], tag="transfer_limit")
                        dpg.add_button(label="Save", callback=save_callback)
                with dpg.menu(label="Editor"):
                    dpg.add_menu_item(label="Theme")
                    dpg.add_menu_item(label="Toggle Fullscreen", callback=fullscreen_callback)
                    dpg.add_menu_item(label="Update", callback=fullscreen_callback)
                with dpg.menu(label="Engine"):
                    dpg.add_text("Maximum Players:")
                    dpg.add_slider_int(default_value=data["defaultMaxPlayers"], tag="max_players")
                    dpg.add_text("Server Life Span:")
                    dpg.add_slider_int(default_value=data["lifeSpanHours"], max_value=6, tag="server_life_span")
                    dpg.add_text("Physics Engine:")
                    dpg.add_listbox(items=['PlanckJS', 'Box2dWeb', 'Box2d es6'], tag="physics_engine")
                    dpg.add_text("Client Physics Engine:")
                    dpg.add_listbox(items=['PlanckJS', 'Box2dWeb', 'Box2d es6'], tag="client_physics_engine")
                    dpg.add_text("Rendering Filter:")
                    dpg.add_listbox(items=['Smooth', 'Pixel Art'], tag="rendering_filter")
                    dpg.add_text("Client-side predicted movement:")
                    dpg.add_checkbox(default_value=data["clientSidePredictionEnabled"], tag="predicted_movement")
                    dpg.add_text("Physics frame rate:")
                    dpg.add_slider_int(default_value=15, max_value=60, tag="physics_frame_rate")
                    dpg.add_text("Gravity:")
                    dpg.add_slider_int(label="x", default_value=0, tag="gravity_x")
                    dpg.add_slider_int(label="y", default_value=0, tag="gravity_y")
                    dpg.add_text("Allow duplicate IP's:")
                    dpg.add_checkbox(default_value=data["allowDuplicateIPS"], tag="duplicate_ips")
                    dpg.add_button(label="Save", callback=save_callback)
                    
                with dpg.menu(label="UI"):
                    print("UI")
                with dpg.menu(label="Map"):
                    print("Map")
                with dpg.menu(label="Title Screen"):
                    print("Title Screen")
                with dpg.menu(label="Moderation"):
                    print("Moderation")
                with dpg.menu(label="Mod/Lobby"):
                    print("Mod/Lobby")


def save_callback(sender):
    with open("taro2/src/game.json") as f:
        data = json.load(f)
        data["title"] = dpg.get_value("game_name")
        data["gameSlug"] = dpg.get_value("game_slug")
        if dpg.get_value("repository_access") == "Private":
            data["access"] = "private"
        else:
            data["access"] = "public"
        data["enableVideoChat"] = dpg.get_value("enable_video_chat")
        data["hidden"] = dpg.get_value("hidden")
        data["enablePersistedData"] = dpg.get_value("enable_persistent_data")
        data["contextMenuEnabled"] = dpg.get_value("context_menu")
        data["dailyCoinTransferLimit"] = dpg.get_value("transfer_limit")
        data["defaultMaxPlayers"] = dpg.get_value("max_players")
        data["lifeSpanHours"] = dpg.get_value("server_life_span")
        data["clientSidePredictionEnabled"] = dpg.get_value("predicted_movement")
        data["frameRate"] = dpg.get_value("physics_frame_rate")
        data["allowDuplicateIPS"] = dpg.get_value("duplicate_ips")
        data["data"]["settings"]["gravity"]["x"] = dpg.get_value("gravity_x")
        data["data"]["settings"]["gravity"]["y"] = dpg.get_value("gravity_y")
        json.dump(data, open("taro2/src/game.json", "w"), indent = 4)

def fullscreen_callback():
    dpg.toggle_viewport_fullscreen()
