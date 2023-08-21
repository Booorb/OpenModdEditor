import dearpygui.dearpygui as dpg
import json
import shutil
import matplotlib
import numpy
from update import update_project_callback


def import_map_callback(sender, app_data, user_data):
    with open(app_data["file_path_name"]) as f:
        map = json.load(f)
        with open(gameFolder + "/taro2/src/game.json") as f:
            data = json.load(f)
            data["data"]["map"]["layers"] = map["layers"]
            json.dump(data, open(gameFolder + "/taro2/src/game.json", "w"), indent=4)


def edit_callback():
    with open("settings.json") as f:
        settings = json.load(f)
        global gameFolder
        gameFolder = settings["gameFolder"]
        if dpg.does_item_exist("game_settings"):
            dpg.show_item("game_settings")
        else:
            with dpg.window(label="Settings", tag="game_settings"):
                with dpg.menu_bar():
                    with dpg.menu(label="General"):
                        with open(gameFolder + "/taro2/src/game.json") as f:
                            data = json.load(f)
                            dpg.add_text("Game Name:")
                            dpg.add_input_text(tag="game_name")
                            if "title" in data.keys():
                                dpg.set_value(value=data["title"], item="game_name")
                            else:
                                dpg.set_value(value="title", item="game_name")
                            dpg.add_text("Game Slug:")
                            dpg.add_input_text(tag="game_slug")
                            if "gameSlug" in data.keys():
                                dpg.set_value(value=data["gameSlug"], item="game_slug")
                            else:
                                dpg.set_value(value="gameSlug", item="game_slug")
                            dpg.add_text("Repository Access:")
                            dpg.add_combo(
                                items=["Open Source", "Private"],
                                tag="repository_access",
                            )
                            if "access" in data.keys():
                                if data["access"] == "private":
                                    dpg.set_value(
                                        value="Private", item="repository_access"
                                    )
                                else:
                                    dpg.set_value(
                                        value="Open Source", item="repository_access"
                                    )
                            dpg.add_text("Enable video chat:")
                            if (
                                "enableVideoChat" in data.keys()
                                and data["enableVideoChat"] is not None
                            ):
                                dpg.add_checkbox(
                                    default_value=data["enableVideoChat"],
                                    tag="enable_video_chat",
                                )
                            else:
                                dpg.add_checkbox(
                                    tag="enable_video_chat",
                                )
                            dpg.add_text("Hidden:")
                            if "hidden" in data.keys() and data["hidden"] is not None:
                                dpg.add_checkbox(
                                    default_value=data["hidden"], tag="hidden"
                                )
                            else:
                                dpg.add_checkbox(tag="hidden")
                            dpg.add_text("Enable Data Saving:")
                            if (
                                "enablePersistedData" in data.keys()
                                and data["enablePersistedData"] is not None
                            ):
                                dpg.add_checkbox(
                                    default_value=data["enablePersistedData"],
                                    tag="enable_persistent_data",
                                )
                            else:
                                dpg.add_checkbox(
                                    tag="enable_persistent_data",
                                )
                            dpg.add_text("Enable Context Menu:")
                            if (
                                "contextMenuEnabled" in data.keys()
                                and data["contextMenuEnabled"] is not None
                            ):
                                dpg.add_checkbox(
                                    default_value=data["contextMenuEnabled"],
                                    tag="context_menu",
                                )
                            else:
                                dpg.add_checkbox(tag="context_menu")
                            dpg.add_text("Disable ads in portals:")
                            if (
                                "disableAdsPortals" in data.keys()
                                and data["disableAdsPortals"] is not None
                            ):
                                dpg.add_checkbox(
                                    default_value=data["disableAdsPortals"],
                                    tag="ads_in_portals",
                                )
                            else:
                                dpg.add_checkbox(
                                    tag="ads_in_portals",
                                )
                            dpg.add_text("Daily coin transfer limit:")
                            if "dailyCoinTransferLimit" in data.keys():
                                dpg.add_slider_int(
                                    default_value=data["dailyCoinTransferLimit"],
                                    tag="transfer_limit",
                                )
                            else:
                                dpg.add_slider_int(
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
                        if "defaultMaxPlayers" in data.keys():
                            dpg.add_slider_int(
                                default_value=data["defaultMaxPlayers"],
                                tag="max_players",
                            )
                        else:
                            dpg.add_slider_int(tag="max_players")
                        dpg.add_text("Server Life Span:")
                        if "lifeSpanHours" in data.keys():
                            dpg.add_slider_int(
                                default_value=data["lifeSpanHours"],
                                max_value=6,
                                tag="server_life_span",
                            )
                        else:
                            dpg.add_slider_int(
                                max_value=6,
                                tag="server_life_span",
                            )
                        dpg.add_text("Physics Engine:")
                        dpg.add_combo(
                            items=["PlanckJS", "Box2dWeb", "Box2d es6"],
                            tag="physics_engine",
                        )
                        if "physicsEngine" in data.keys():
                            if data["physicsEngine"] == "planck":
                                dpg.set_value(value="PlanckJS", item="physics_engine")
                            elif data["physicsEngine"] == "box2dweb":
                                dpg.set_value(value="Box2dWeb", item="physics_engine")
                            else:
                                dpg.set_value(value="Box2d es6", item="physics_engine")
                        dpg.add_text("Client Physics Engine:")
                        dpg.add_combo(
                            items=["PlanckJS", "Box2dWeb", "Box2d es6"],
                            tag="client_physics_engine",
                        )
                        if "clientPhysicsEngine" in data.keys():
                            if data["clientPhysicsEngine"] == "planck":
                                dpg.set_value(
                                    value="PlanckJS", item="client_physics_engine"
                                )
                            elif data["clientPhysicsEngine"] == "box2dweb":
                                dpg.set_value(
                                    value="Box2dWeb", item="client_physics_engine"
                                )
                            else:
                                dpg.set_value(
                                    value="Box2d es6", item="client_physics_engine"
                                )
                        dpg.add_text("Rendering Filter:")
                        dpg.add_combo(
                            items=["Smooth", "Pixel Art"], tag="rendering_filter"
                        )
                        if "renderingFilter" in data.keys():
                            if data["renderingFilter"] == "smooth":
                                dpg.set_value(value="Smooth", item="rendering_filter")
                            else:
                                dpg.set_value(
                                    value="Pixel Art", item="rendering_filter"
                                )
                        dpg.add_text("Client-side predicted movement:")
                        if (
                            "clientSidePredictionEnabled" in data.keys()
                            and data["clientSidePredictionEnabled"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["clientSidePredictionEnabled"],
                                tag="predicted_movement",
                            )
                        else:
                            dpg.add_checkbox(tag="predicted_movement")
                        dpg.add_text("Continuous Physics:")
                        if (
                            "continuousPhysics" in data["data"]["settings"].keys()
                            and data["data"]["settings"]["continuousPhysics"]
                            is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["data"]["settings"][
                                    "continuousPhysics"
                                ],
                                tag="continuous_physics",
                            )
                        else:
                            dpg.add_checkbox(tag="continuous_physics")
                        dpg.add_text("Physics frame rate:")
                        dpg.add_slider_int(
                            default_value=15, max_value=60, tag="physics_frame_rate"
                        )
                        dpg.add_text("Gravity:")
                        dpg.add_slider_int(label="x", default_value=0, tag="gravity_x")
                        dpg.add_slider_int(label="y", default_value=0, tag="gravity_y")
                        dpg.add_text("Allow duplicate IP's:")
                        if (
                            "allowDuplicateIPS" in data.keys()
                            and data["allowDuplicateIPS"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["allowDuplicateIPS"],
                                tag="duplicate_ips",
                            )
                        else:
                            dpg.add_checkbox(tag="duplicate_ips")
                        dpg.add_button(label="Save", callback=save_callback)

                    with dpg.menu(label="UI"):
                        dpg.add_text("Display Leaderboard:")
                        if (
                            "displayScoreboard" in data["data"]["settings"].keys()
                            and data["data"]["settings"]["displayScoreboard"]
                            is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["data"]["settings"][
                                    "displayScoreboard"
                                ],
                                tag="display_leaderboard",
                            )
                        else:
                            dpg.add_checkbox(tag="display_leaderboard")
                        dpg.add_text("For leaderboard, use:")
                        attribute_list = []
                        if "attributeTypes" in data["data"].keys():
                            for attribute in data["data"]["attributeTypes"]:
                                attribute_list.append(attribute)
                        if "scoreAttributeId" in data["data"]["settings"].keys():
                            dpg.add_combo(
                                default_value=data["data"]["settings"][
                                    "scoreAttributeId"
                                ],
                                items=attribute_list,
                                tag="leaderboard_attribute",
                            )
                        else:
                            dpg.add_combo(
                                items=attribute_list, tag="leaderboard_attribute"
                            )
                        dpg.add_text("Prettify Leaderboard:")
                        if (
                            "prettifyingScoreboard" in data["data"]["settings"].keys()
                            and data["data"]["settings"]["prettifyingScoreboard"]
                            is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["data"]["settings"][
                                    "prettifyingScoreboard"
                                ],
                                tag="prettify_leaderboard",
                            )
                        else:
                            dpg.add_checkbox(tag="prettify_leaderboard")
                        dpg.add_text("Default Camera Zoom:")
                        if (
                            "default"
                            in data["data"]["settings"]["camera"]["zoom"].keys()
                        ):
                            dpg.add_slider_int(
                                default_value=data["data"]["settings"]["camera"][
                                    "zoom"
                                ]["default"],
                                min_value=250,
                                max_value=1500,
                                tag="camera_zoom",
                            )
                        else:
                            dpg.add_slider_int(
                                min_value=250,
                                max_value=1500,
                                tag="camera_zoom",
                            )
                        dpg.add_text("Camera Tracking Speed:")
                        if "trackingDelay" in data["data"]["settings"]["camera"].keys():
                            dpg.add_slider_int(
                                default_value=data["data"]["settings"]["camera"][
                                    "trackingDelay"
                                ],
                                min_value=1,
                                max_value=60,
                                tag="camera_tracking_speed",
                            )
                        else:
                            dpg.add_slider_int(
                                min_value=1,
                                max_value=60,
                                tag="camera_tracking_speed",
                            )
                        dpg.add_text("Add stroke to name labels and attribute bars:")
                        if (
                            "addStrokeToNameAndAttributes"
                            in data["data"]["settings"].keys()
                            and data["data"]["settings"]["addStrokeToNameAndAttributes"]
                            is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["data"]["settings"][
                                    "addStrokeToNameAndAttributes"
                                ],
                                tag="add_stroke",
                            )
                        else:
                            dpg.add_checkbox(tag="add_stroke")
                        dpg.add_text("Height Based Z-Index:")
                        if (
                            "heightBasedZIndex" in data.keys()
                            and data["heightBasedZIndex"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["heightBasedZIndex"],
                                tag="height_based_z_index",
                            )
                        else:
                            dpg.add_checkbox(tag="height_based_z_index")
                        dpg.add_button(label="Save", callback=save_callback)
                    with dpg.menu(label="Map"):
                        dpg.add_text("Tileset Link:")
                        if "image" in data["data"]["map"]["tilesets"][0].keys():
                            dpg.add_input_text(
                                default_value=data["data"]["map"]["tilesets"][0][
                                    "image"
                                ],
                                tag="tileset_link",
                            )
                        else:
                            dpg.add_input_text(tag="tileset_link")
                        dpg.add_text("Map Out of Bounds Color:")
                        if "mapBackgroundColor" in data.keys():
                            dpg.add_color_edit(
                                default_value=settings["projects"][
                                    dpg.get_value("game_name")
                                ]["mapBackgroundColor"],
                                tag="background_color",
                            )
                        else:
                            dpg.add_color_edit(tag="background_color")
                        dpg.add_text("Disable tile scaling:")
                        if (
                            "dontResize" in data.keys()
                            and data["dontResize"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["dontResize"], tag="scale_tiles"
                            )
                        else:
                            dpg.add_checkbox(tag="scale_tiles")
                        dpg.add_text("Map Size:")
                        dpg.add_text("width:")
                        if "width" in data["data"]["map"].keys():
                            dpg.add_slider_int(
                                default_value=data["data"]["map"]["width"],
                                tag="map_width",
                            )
                        else:
                            dpg.add_slider_int(tag="map_width")
                        dpg.add_text("height:")
                        if "height" in data["data"]["map"].keys():
                            dpg.add_slider_int(
                                default_value=data["data"]["map"]["height"],
                                tag="map_height",
                            )
                        else:
                            dpg.add_slider_int(tag="map_height")
                        dpg.add_text("Tiled Import:")
                        dpg.add_button(
                            label="Upload Tiled Map JSON",
                            callback=lambda: dpg.show_item("import_map"),
                        )
                        dpg.add_button(label="Save", callback=save_callback)
                    with dpg.menu(label="Title Screen"):
                        dpg.add_text("Menu")
                        dpg.add_separator()
                        dpg.add_text("Game Description:")
                        if "menudiv" in data["data"]["settings"].keys():
                            dpg.add_input_text(
                                default_value=data["data"]["settings"]["menudiv"],
                                tag="game_description",
                                multiline=True,
                            )
                        else:
                            dpg.add_input_text(tag="game_description")
                        dpg.add_text("Gameplay Instructions:")
                        if "gamePlayInstructions" in data.keys():
                            dpg.add_input_text(
                                default_value=data["gamePlayInstructions"],
                                tag="gameplay_instructions",
                                multiline=True,
                            )
                        else:
                            dpg.add_input_text(tag="gameplay_instructions")
                        dpg.add_text("Images")
                        dpg.add_separator()
                        dpg.add_text("Logo Image:")
                        if "logo" in data["data"]["settings"]["images"].keys():
                            dpg.add_input_text(
                                default_value=data["data"]["settings"]["images"][
                                    "logo"
                                ],
                                tag="logo_link",
                            )
                        else:
                            dpg.add_input_text(tag="logo_link")
                        dpg.add_text("Cover Image:")
                        if "cover" in data["data"]["settings"]["images"].keys():
                            dpg.add_input_text(
                                default_value=data["data"]["settings"]["images"][
                                    "cover"
                                ],
                                tag="cover_link",
                            )
                        else:
                            dpg.add_input_text(tag="cover_link")
                        dpg.add_text("Game Icon:")
                        if "icon" in data["data"]["settings"]["images"].keys():
                            dpg.add_input_text(
                                default_value=data["data"]["settings"]["images"][
                                    "icon"
                                ],
                                tag="icon_link",
                            )
                        else:
                            dpg.add_input_text(tag="icon_link")
                        dpg.add_text("Social")
                        dpg.add_separator()
                        dpg.add_text("Discord invite link:")
                        if "discordInviteLink" in data.keys():
                            dpg.add_input_text(
                                default_value=data["discordInviteLink"],
                                tag="discord_link",
                            )
                        else:
                            dpg.add_input_text(tag="discord_link")
                        dpg.add_text("Twitter link:")
                        if "twitterLink" in data.keys():
                            dpg.add_input_text(
                                default_value=data["twitterLink"], tag="twitter_link"
                            )
                        else:
                            dpg.add_input_text(tag="twitter_link")
                        dpg.add_text("Facebook link:")
                        if "facebookLink" in data.keys():
                            dpg.add_input_text(
                                default_value=data["facebookLink"], tag="facebook_link"
                            )
                        else:
                            dpg.add_input_text(tag="facebook_link")
                        dpg.add_text("Youtube link:")
                        if "youtubeLink" in data.keys():
                            dpg.add_input_text(
                                default_value=data["youtubeLink"], tag="youtube_link"
                            )
                        else:
                            dpg.add_input_text(tag="youtube_link")
                        dpg.add_text("More IO Games link for iogames.space:")
                        if (
                            "moreIoGames" in data.keys()
                            and data["moreIoGames"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["moreIoGames"], tag="iogames_link"
                            )
                        else:
                            dpg.add_checkbox(tag="iogames_link")
                        dpg.add_button(label="Save", callback=save_callback)
                    with dpg.menu(label="Mod/Lobby"):
                        dpg.add_text("Allow Modding:")
                        if (
                            "isModdable" in data.keys()
                            and data["isModdable"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["isModdable"], tag="allow_modding"
                            )
                        else:
                            dpg.add_checkbox(tag="allow_modding")
                        dpg.add_text("Enable Lobby:")
                        if (
                            "isLobbyEnabled" in data.keys()
                            and data["isLobbyEnabled"] is not None
                        ):
                            dpg.add_checkbox(
                                default_value=data["isLobbyEnabled"], tag="enable_lobby"
                            )
                        else:
                            dpg.add_checkbox(tag="enable_lobby")
                        dpg.add_button(
                            label="Save",
                            callback=save_callback,
                        )


def save_callback(sender):
    with open(gameFolder + "/taro2/src/game.json") as f:
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
        data["data"]["settings"]["continuousPhysics"] = dpg.get_value(
            "continuous_physics"
        )
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
        data["data"]["settings"]["scoreAttributeId"] = dpg.get_value(
            "leaderboard_attribute"
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
        data["data"]["map"]["tilesets"][0]["image"] = dpg.get_value("tileset_link")
        backgroundColor255Range = list(map(int, dpg.get_value("background_color")))
        backgroundColor1Range = numpy.divide(backgroundColor255Range, 255)
        backgroundColorHex = matplotlib.colors.to_hex(backgroundColor1Range)
        data["mapBackgroundColor"] = backgroundColorHex
        data["dontResize"] = dpg.get_value("scale_tiles")
        data["data"]["map"]["width"] = dpg.get_value("map_width")
        data["data"]["map"]["height"] = dpg.get_value("map_height")
        data["data"]["settings"]["menudiv"] = dpg.get_value("game_description")
        data["gamePlayInstructions"] = dpg.get_value("gameplay_instructions")
        data["data"]["settings"]["images"]["cover"] = dpg.get_value("cover_link")
        data["data"]["settings"]["images"]["logo"] = dpg.get_value("logo_link")
        data["data"]["settings"]["images"]["icon"] = dpg.get_value("icon_link")
        data["discordInviteLink"] = dpg.get_value("discord_link")
        data["twitterLink"] = dpg.get_value("twitter_link")
        data["facebookLink"] = dpg.get_value("facebook_link")
        data["youtubeLink"] = dpg.get_value("youtube_link")
        data["moreIoGames"] = dpg.get_value("iogames_link")
        data["isModdable"] = dpg.get_value("allow_modding")
        data["isLobbyEnabled"] = dpg.get_value("enable_lobby")
        json.dump(data, open(gameFolder + "/taro2/src/game.json", "w"), indent=4)
        with open("settings.json") as f:
            settings = json.load(f)
            settings["projects"][dpg.get_value("game_name")][
                "mapBackgroundColor"
            ] = dpg.get_value("background_color")
            json.dump(settings, open("settings.json", "w"), indent=4)


def fullscreen_callback():
    dpg.toggle_viewport_fullscreen()
