import dearpygui.dearpygui as dpg
import json
from update import update_project_callback


def back_callback():
    if dpg.does_item_exist("game_settings"):
        dpg.show_item("default_window")
        dpg.set_primary_window("default_window", True)


def edit_callback():
    if dpg.does_item_exist("game_settings"):
        dpg.show_item("game_settings")
        dpg.set_primary_window("game_settings", True)
    else:
        with dpg.window(label="Settings", tag="game_settings"):
            dpg.set_primary_window("game_settings", True)
            with dpg.menu_bar():
                with dpg.menu(label="General"):
                    with open("taro2/src/game.json") as f:
                        data = json.load(f)
                        dpg.add_text("Game Name:")
                        dpg.add_input_text(tag="game_name")
                        dpg.set_value(value=data["title"], item="game_name")
                        dpg.add_text("Game Slug:")
                        dpg.add_input_text(tag="game_slug")
                        dpg.set_value(value=data["gameSlug"], item="game_slug")
                        dpg.add_text("Repository Access:")
                        dpg.add_listbox(
                            items=["Open Source", "Private"], tag="repository_access"
                        )
                        if data["access"] == "private":
                            dpg.set_value(value="Private", item="repository_access")
                        else:
                            dpg.set_value(value="Open Source", item="repository_access")
                        dpg.add_text("Enable video chat:")
                        dpg.add_checkbox(
                            default_value=data["enableVideoChat"],
                            tag="enable_video_chat",
                        )
                        dpg.add_text("Hidden:")
                        dpg.add_checkbox(default_value=data["hidden"], tag="hidden")
                        dpg.add_text("Enable Data Saving:")
                        dpg.add_checkbox(
                            default_value=data["enablePersistedData"],
                            tag="enable_persistent_data",
                        )
                        dpg.add_text("Enable Context Menu:")
                        dpg.add_checkbox(
                            default_value=data["contextMenuEnabled"], tag="context_menu"
                        )
                        dpg.add_text("Disable ads in portals:")
                        dpg.add_checkbox(
                            default_value=data["disableAdsPortals"],
                            tag="ads_in_portals",
                        )
                        dpg.add_text("Daily coin transfer limit:")
                        dpg.add_slider_int(
                            default_value=data["dailyCoinTransferLimit"],
                            tag="transfer_limit",
                        )
                        dpg.add_button(label="Save", callback=save_callback)
                with dpg.menu(label="Editor"):
                    dpg.add_menu_item(label="Theme")
                    dpg.add_menu_item(
                        label="Toggle Fullscreen", callback=fullscreen_callback
                    )
                    dpg.add_menu_item(
                        label="Update",
                        callback=update_project_callback,
                    )
                with dpg.menu(label="Engine"):
                    dpg.add_text("Maximum Players:")
                    dpg.add_slider_int(
                        default_value=data["defaultMaxPlayers"], tag="max_players"
                    )
                    dpg.add_text("Server Life Span:")
                    dpg.add_slider_int(
                        default_value=data["lifeSpanHours"],
                        max_value=6,
                        tag="server_life_span",
                    )
                    dpg.add_text("Physics Engine:")
                    dpg.add_listbox(
                        items=["PlanckJS", "Box2dWeb", "Box2d es6"],
                        tag="physics_engine",
                    )
                    if data["physicsEngine"] == "planck":
                        dpg.set_value(value="PlanckJS", item="physics_engine")
                    elif data["physicsEngine"] == "box2dweb":
                        dpg.set_value(value="Box2dWeb", item="physics_engine")
                    else:
                        dpg.set_value(value="Box2d es6", item="physics_engine")
                    dpg.add_text("Client Physics Engine:")
                    dpg.add_listbox(
                        items=["PlanckJS", "Box2dWeb", "Box2d es6"],
                        tag="client_physics_engine",
                    )
                    if data["clientPhysicsEngine"] == "planck":
                        dpg.set_value(value="PlanckJS", item="client_physics_engine")
                    elif data["clientPhysicsEngine"] == "box2dweb":
                        dpg.set_value(value="Box2dWeb", item="client_physics_engine")
                    else:
                        dpg.set_value(value="Box2d es6", item="client_physics_engine")
                    dpg.add_text("Rendering Filter:")
                    dpg.add_listbox(
                        items=["Smooth", "Pixel Art"], tag="rendering_filter"
                    )
                    if data["renderingFilter"] == "smooth":
                        dpg.set_value(value="Smooth", item="rendering_filter")
                    else:
                        dpg.set_value(value="Pixel Art", item="rendering_filter")
                    dpg.add_text("Client-side predicted movement:")
                    dpg.add_checkbox(
                        default_value=data["clientSidePredictionEnabled"],
                        tag="predicted_movement",
                    )
                    dpg.add_text("Physics frame rate:")
                    dpg.add_slider_int(
                        default_value=15, max_value=60, tag="physics_frame_rate"
                    )
                    dpg.add_text("Gravity:")
                    dpg.add_slider_int(label="x", default_value=0, tag="gravity_x")
                    dpg.add_slider_int(label="y", default_value=0, tag="gravity_y")
                    dpg.add_text("Allow duplicate IP's:")
                    dpg.add_checkbox(
                        default_value=data["allowDuplicateIPS"], tag="duplicate_ips"
                    )
                    dpg.add_button(label="Save", callback=save_callback)

                with dpg.menu(label="UI"):
                    dpg.add_text("Display Leaderboard:")
                    dpg.add_checkbox(
                        default_value=data["data"]["settings"]["displayScoreboard"],
                        tag="display_leaderboard",
                    )
                    dpg.add_text("Prettify Leaderboard:")
                    dpg.add_checkbox(
                        default_value=data["data"]["settings"]["prettifyingScoreboard"],
                        tag="prettify_leaderboard",
                    )
                    dpg.add_text("Default Camera Zoom:")
                    dpg.add_slider_int(
                        default_value=data["data"]["settings"]["camera"]["zoom"][
                            "default"
                        ],
                        min_value=250,
                        max_value=1500,
                        tag="camera_zoom",
                    )
                    dpg.add_text("Camera Tracking Speed:")
                    dpg.add_slider_int(
                        default_value=data["data"]["settings"]["camera"][
                            "trackingDelay"
                        ],
                        min_value=1,
                        max_value=60,
                        tag="camera_tracking_speed",
                    )
                    dpg.add_text("Add stroke to name labels and attribute bars:")
                    dpg.add_checkbox(
                        default_value=data["data"]["settings"][
                            "addStrokeToNameAndAttributes"
                        ],
                        tag="add_stroke",
                    )
                    dpg.add_text("Height Based Z-Index:")
                    dpg.add_checkbox(
                        default_value=data["heightBasedZIndex"],
                        tag="height_based_z_index",
                    )
                    dpg.add_button(label="Save", callback=save_callback)
                with dpg.menu(label="Map"):
                    print("Map")
                with dpg.menu(label="Title Screen"):
                    print("Title Screen")
                with dpg.menu(label="Mod/Lobby"):
                    dpg.add_text("Allow Modding:")
                    dpg.add_checkbox(
                        default_value=data["isModdable"], tag="allow_modding"
                    )
                    dpg.add_text("Enable Lobby:")
                    dpg.add_checkbox(
                        default_value=data["isLobbyEnabled"], tag="enable_lobby"
                    )
                    dpg.add_button(label="Save", callback=save_callback)

            dpg.add_button(label="Back", tag="back_button", callback=back_callback)


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
        data["disableAdsPortals"] = dpg.get_value("ads_in_portals")
        data["dailyCoinTransferLimit"] = dpg.get_value("transfer_limit")
        data["defaultMaxPlayers"] = dpg.get_value("max_players")
        data["lifeSpanHours"] = dpg.get_value("server_life_span")
        if dpg.get_value("physics_engine") == "PlanckJS":
            data["physicsEngine"] = "planck"
        elif dpg.get_value("physics_engine") == "Box2dWeb":
            data["physicsEngine"] = "box2dweb"
        else:
            data["physicsEngine"] = "box2dts"
        if dpg.get_value("client_physics_engine") == "PlanckJS":
            data["clientPhysicsEngine"] = "planck"
        elif dpg.get_value("client_physics_engine") == "Box2dWeb":
            data["clientPhysicsEngine"] = "box2dweb"
        else:
            data["clientPhysicsEngine"] = "box2dts"
        if dpg.get_value("rendering_filter") == "Smooth":
            data["renderingFilter"] = "smooth"
        else:
            data["renderingFilter"] = "pixelArt"
        data["clientSidePredictionEnabled"] = dpg.get_value("predicted_movement")
        data["frameRate"] = dpg.get_value("physics_frame_rate")
        data["allowDuplicateIPS"] = dpg.get_value("duplicate_ips")
        data["data"]["settings"]["gravity"]["x"] = dpg.get_value("gravity_x")
        data["data"]["settings"]["gravity"]["y"] = dpg.get_value("gravity_y")
        data["data"]["settings"]["displayScoreboard"] = dpg.get_value(
            "display_leaderboard"
        )
        data["data"]["settings"]["prettifyingScoreboard"] = dpg.get_value(
            "prettify_leaderboard"
        )
        data["data"]["settings"]["camera"]["zoom"]["default"] = dpg.get_value(
            "camera_zoom"
        )
        data["data"]["settings"]["camera"]["trackingDelay"] = dpg.get_value(
            "camera_tracking_speed"
        )
        data["data"]["settings"]["addStrokeToNameAndAttributes"] = dpg.get_value(
            "add_stroke"
        )
        data["heightBasedZIndex"] = dpg.get_value("height_based_z_index")
        data["isModdable"] = dpg.get_value("allow_modding")
        data["isLobbyEnabled"] = dpg.get_value("enable_lobby")
        json.dump(data, open("taro2/src/game.json", "w"), indent=4)


def fullscreen_callback():
    dpg.toggle_viewport_fullscreen()
