import sys

from board import *
from player import Player
from ui import ConsoleUI


def game_start_routine():
    ui.game.welcome()
    player1_name, player2_name = ui.game.enter_names()
    players = [Player(1, player1_name), Player(2, player2_name)]
    return players


def game_step(player):
    ui.game.turn_start_roll_dice(player)
    steps, position = player.move()
    ui.game.dice_landed(steps, position)
    accessible_items = game_board.item_list[player.position]
    ui.game.show_accessible_items(accessible_items)
    for item in accessible_items:
        ui.game.consider_an_item(item)
        if isinstance(item, Property):
            if item.owner_id == 0:
                choice = ui.property.ask_buy_property(item, player)
                if choice == "Y":
                    if player.buy_property(item):
                        ui.property.buy_property_success(item, player)
                    else:
                        ui.property.buy_property_failure(item)
                else:
                    ui.property.player_refuse_buy_property()
            elif item.owner_id == player.player_id:
                choice = ui.property.ask_upgrade_property(item)
                if choice == "Y":
                    status = player.upgrade_property(item)
                    if status == 1:
                        ui.property.upgrade_property_success(item, player)
                    elif status == 0:
                        ui.property.upgrade_property_failure_max_level(item)
                    elif status == -1:
                        ui.property.upgrade_property_failure_money(item)
                else:
                    ui.property.player_refuse_upgrade_property()
            else:
                target_player = players_list[item.owner_id - 1]
                ui.property.need_to_pay_rent(item, target_player)
                if player.pay_rent(item, target_player):
                    ui.property.pay_rent_success(item, player, target_player)
                else:
                    ui.property.pay_rent_failure(item)
                    ui.game.won(target_player)
                    sys.exit()
                    # TODO: Generalise to more than 2 players

        elif isinstance(item, Tower):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, GoodChest):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, BadChest):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Hotel):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Park):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Pond):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Bank):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Supermarket):
            ui.game.feature_not_available()
            #TODO

        elif isinstance(item, Restaurant):
            ui.game.feature_not_available()
            #TODO


game_board = Board()
ui = ConsoleUI()
players_list = game_start_routine()
while True:
    for current_player in players_list:
        game_step(current_player)