import sys

from board import *
from player import Player
from ui import ConsoleUI


def game_start_routine():
    ui.game.welcome()
    player1_name, player2_name = ui.game.enter_names()
    players = [Player(1, player1_name), Player(2, player2_name)]
    return players


def game_handle_property(item, player):
    if item.owner_id == 0:
        choice = ui.property.ask_buy_property(item, player)
        if choice == "Y":
            if player.buy_property(item):
                ui.property.buy_property_success(item, player)
                if game_board.check_for_complete_group(item.group, player):
                    ui.property.player_own_complete_group(item.group)
            else:
                ui.property.buy_property_failure(item)
        else:
            ui.game.alright_press_enter_continue()
    elif item.owner_id == player.player_id:
        choice = ui.property.ask_upgrade_property(item, player)
        if choice == "Y":
            status = player.upgrade_property(item)
            if status == 1:
                ui.property.upgrade_property_success(item, player)
            elif status == 0:
                ui.property.upgrade_property_failure_max_level(item)
            elif status == -1:
                ui.property.upgrade_property_failure_money(item)
        else:
            ui.game.alright_press_enter_continue()
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


def game_handle_tower(item, player):
    if player.receive_salary_if_applicable(item):
        ui.tower.receive_salary(player, item)
    choice = ui.tower.ask_if_looking_for_jobs()
    if choice == "Y":
        choice_number = ui.tower.show_jobs_wait_application(player, item)
        if choice_number in ["1", "2", "3"]:
            target_job = item.jobs[int(choice_number) - 1]
            status = player.apply_for_job(target_job)
            if status == -1:
                ui.tower.apply_job_failure_money(target_job)
            elif status == 0:
                ui.tower.apply_job_failure_reject()
            elif status == 1:
                ui.tower.apply_job_success(player)
        else:
            ui.game.alright_press_enter_continue()
    else:
        ui.game.alright_press_enter_continue()


def game_handle_chest(chest_type, item, player):
    ui.chest.show_distribution_wait_draw_card(chest_type)
    rarity, card = item.draw_card(player)
    ui.chest.display_card(rarity, card)
    item.given_card_take_action(card, player, players_list, game_board)
    ui.chest.effect_claimed(chest_type)


def game_handle_pond(item, player):
    fishing_rods_in_backpack = [x for x in player.backpack if isinstance(x, FishingRod)]
    if len(fishing_rods_in_backpack) > 0:
        choice_number, bound = ui.pond.show_fishing_rods_wait_choice(fishing_rods_in_backpack)
        if choice_number.isdigit() and 1 <= int(choice_number) <= bound:
            fishing_rod = fishing_rods_in_backpack[int(choice_number) - 1]
            result = item.get_random_fish(player, fishing_rod)
            if result is not None:
                name, description, price = result
                player.backpack.append(FishForSale(name, price))
                ui.pond.show_fish_caught(name, description, price)
            else:
                ui.pond.catch_nothing()
        else:
            ui.game.alright_press_enter_continue()
    else:
        ui.pond.no_fishing_rod()


def game_handle_restaurant(item, player):
    choice_number = ui.restaurant.show_menu_wait_choice(player)
    if choice_number in ["1", "2", "3", "4", "5"]:
        status = item.buy_food(int(choice_number), player)
        if status == 1:
            ui.restaurant.buy_food_success_gain_luck(player)
        elif status == 0:
            ui.restaurant.buy_food_success_not_gain_luck()
        elif status == -1:
            ui.restaurant.buy_food_failure_money()
    else:
        ui.game.alright_press_enter_continue()


def game_step(player):
    ui.game.turn_start_roll_dice(player)
    steps, position = player.move()
    ui.game.dice_landed(steps, position)
    accessible_items = game_board.item_list[player.position]
    ui.game.show_accessible_items(accessible_items)
    for item in accessible_items:
        ui.game.consider_an_item(item)
        if isinstance(item, Property):
            game_handle_property(item, player)
        elif isinstance(item, Tower):
            game_handle_tower(item, player)
        elif isinstance(item, GoodChest):
            game_handle_chest("good", item, player)
        elif isinstance(item, BadChest):
            game_handle_chest("bad", item, player)
        elif isinstance(item, Park):
            ui.game.feature_not_available()
            #TODO
        elif isinstance(item, Pond):
            game_handle_pond(item, player)
        elif isinstance(item, Bank):
            ui.game.feature_not_available()
            #TODO
        elif isinstance(item, Market):
            ui.game.feature_not_available()
            #TODO
        elif isinstance(item, Restaurant):
            game_handle_restaurant(item, player)

game_board = Board()
ui = ConsoleUI()
players_list = game_start_routine()
while True:
    for current_player in players_list:
        game_step(current_player)