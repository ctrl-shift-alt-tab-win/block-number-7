import copy
import sys

from board import *
from player import Player
from ui import ConsoleUI


def game_start_routine():
    ui.game.welcome()
    num_players = ui.game.enter_num_players()
    players = []
    for i in range(1, num_players+1):
        name = ui.game.enter_player_name(i)
        players.append(Player(i, name))
    return players


def game_end_routine(player):
    ui.game.player_lost(player)
    player.alive = False
    remaining_players = [p for p in players_list if p.alive]
    if len(remaining_players) == 1:
        ui.game.won(remaining_players[0])
        sys.exit()


def game_handle_property(item, player):
    if item.owner_id == 0:
        choice = ui.ownable.ask_if_buy(item, player)
        if choice == "Y":
            if player.buy_ownable(item, has_level=True):
                ui.ownable.buy_success(item, player)
                if game_board.check_for_complete_group(item.group, player):
                    ui.property.player_own_complete_group(item.group)
            else:
                ui.ownable.buy_failure(item)
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
        ui.ownable.need_to_pay_rent(item, target_player)
        if player.pay_rent_ownable(item, target_player):
            ui.ownable.pay_rent_success(item, player, target_player)
        else:
            ui.ownable.pay_rent_failure(item)
            game_end_routine(player)


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
    if rarity in ["Awful", "Awful+", "Awful++"] and player.have_awful_luck_shield():
        player.backpack.remove("Awful Luck Shield")
        ui.chest.awful_luck_shield_activated(player)
    else:
        item.given_card_take_action(card, player, players_list, game_board)
        ui.chest.effect_claimed(chest_type)


def game_handle_park(item, player):
    if item.owner_id == 0:
        choice = ui.ownable.ask_if_buy(item, player)
        if choice == "Y":
            if player.buy_ownable(item, has_level=False):
                ui.ownable.buy_success(item, player)
            else:
                ui.ownable.buy_failure(item)
        else:
            ui.game.alright_press_enter_continue()
    elif item.owner_id == player.player_id:
        choice = ui.park.own_park_ask_if_enter()
        if choice == "Y":
            player.enter_park()
            ui.park.now_inside_park()
        else:
            ui.game.alright_press_enter_continue()
    else:
        target_player = players_list[item.owner_id - 1]
        ui.ownable.need_to_pay_rent(item, target_player)
        if player.pay_rent_ownable(item, target_player):
            ui.ownable.pay_rent_success(item, player, target_player)
        else:
            ui.ownable.pay_rent_failure(item)
            game_end_routine(player)

def game_handle_pond(item, player):
    fishing_rods_in_backpack = [x for x in player.backpack if isinstance(x, FishingRod)]
    if len(fishing_rods_in_backpack) > 0:
        choice_number, bound = ui.pond.show_fishing_rods_wait_choice(fishing_rods_in_backpack)
        if choice_number.isdigit() and 1 <= int(choice_number) <= bound:
            fishing_rod = fishing_rods_in_backpack[int(choice_number) - 1]
            if fishing_rod.level == 4 and player.have_glowing_bait():
                choice = ui.pond.ask_if_use_glowing_bait(player)
                if choice == "Y":
                    ui.pond.attached_glowing_bait()
                    result = item.get_random_fish_glowing_bait(player, fishing_rod)
                else:
                    ui.game.alright_press_enter_continue()
                    result = item.get_random_fish(player, fishing_rod)
            else:
                result = item.get_random_fish(player, fishing_rod)
            if result is not None:
                name, description, price, rarity = result
                ui.pond.show_fish_caught(name, description, price, rarity)
                if len(player.backpack) == player.backpack_limit:
                    ui.game.backpack_full()
                else:
                    player.backpack.append(FishForSale(name, price))
            else:
                ui.pond.catch_nothing()
        else:
            ui.game.alright_press_enter_continue()
    else:
        ui.pond.no_fishing_rod()


def game_handle_bank(item, player):
    if player.loan is None:
        choice = ui.bank.ask_if_take_loan()
        if choice == "Y":
            choice_number = ui.bank.show_loans_wait_choice(item)
            if choice_number in ["1", "2", "3", "4", "5"]:
                selected_loan = item.loan_list[int(choice_number) - 1]
                player.loan = selected_loan
                player.loan_remaining_number_of_payments = selected_loan.number_of_payments
                player.cash += selected_loan.borrow_amount
                ui.bank.borrow_money_success(player, selected_loan)
            else:
                ui.game.alright_press_enter_continue()
        else:
            ui.game.alright_press_enter_continue()
    else:
        ui.bank.need_to_pay_loan(player)
        if player.cash < player.loan.pay_amount_each_time:
            ui.bank.not_enough_money_pay_loan()
            game_end_routine(player)
        else:
            player.cash -= player.loan.pay_amount_each_time
            player.loan_remaining_number_of_payments -= 1
            ui.bank.pay_loan_success(player)
            if player.loan_remaining_number_of_payments == 0:
                player.loan = None
                player.loan_remaining_number_of_payments = None
                ui.bank.fully_repaid_loan()


def game_handle_market(item, player):
    choice_number = ui.market.show_option_buy_sell_wait_choice()
    if choice_number == "1":
        choice_number_inner = ui.market.show_market_buy_wait_choice(player)
        if choice_number_inner in ["1", "2", "3", "4", "5", "6", "7"]:
            if len(player.backpack) == player.backpack_limit:
                ui.game.backpack_full()
            else:
                n = int(choice_number_inner)
                if player.limit_dict[item.market_item_name_list[n - 1]] == 0:
                    ui.market.max_purchase_limit_reached()
                else:
                    if player.cash < item.market_item_price_list[n - 1]:
                        ui.market.not_enough_money_buy_item()
                    else:
                        player.limit_dict[item.market_item_name_list[n - 1]] -= 1
                        player.backpack.append(copy.deepcopy(item.market_item_list[n - 1]))
                        player.cash -= item.market_item_price_list[n - 1]
                        ui.market.purchase_success_item_added_backpack()
        elif choice_number_inner == "8":
            if player.limit_dict[item.market_item_name_list[7]] == 0:
                ui.market.max_purchase_limit_reached()
            else:
                if player.cash < item.market_item_price_list[7]:
                    ui.market.not_enough_money_buy_item()
                else:
                    player.limit_dict[item.market_item_name_list[7]] -= 1
                    player.backpack_limit *= 2
                    player.cash -= item.market_item_price_list[7]
                    ui.market.purchase_success_backpack_upgraded(player)
        else:
            ui.game.alright_press_enter_continue()
    elif choice_number == "2":
        things_for_sale = [x for x in player.backpack if isinstance(x, FishForSale)]
        if len(things_for_sale) == 0:
            ui.market.no_sellable_item()
        else:
            ui.market.show_market_selling_title()
            for thing in things_for_sale:
                choice = ui.market.sell_item_wait_choice(thing)
                if choice == "Y":
                    player.backpack.remove(thing)
                    player.cash += thing.price
                    ui.market.sold_success()
                else:
                    ui.game.alright_press_enter_continue()
    else:
        ui.game.alright_press_enter_continue()


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
    supplied_number = None
    if player.have_controllable_dice():
        choice = ui.game.ask_if_use_controllable_dice(player)
        if choice == "Y":
            number = ui.game.wait_integer_1_6()
            if number in ["1", "2", "3", "4", "5", "6"]:
                supplied_number = int(number)
                player.backpack.remove("Controllable Dice")
            else:
                ui.game.not_enter_integer_1_6()
        else:
            ui.game.alright_press_enter_continue()
    steps, position = player.move(supplied_number)
    ui.game.dice_landed(steps, position)
    if player.position == 101:
        game_board.park.increase_rent()
        ui.park.stuck_in_park_increase_rent()
        return
    if player.position == 102:
        ui.park.stuck_in_park_access_pond()
        game_handle_pond(game_board.pond, player)
        return
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
            game_handle_park(item, player)
        elif isinstance(item, Pond):
            game_handle_pond(item, player)
        elif isinstance(item, Bank):
            game_handle_bank(item, player)
        elif isinstance(item, Market):
            game_handle_market(item, player)
        elif isinstance(item, Restaurant):
            game_handle_restaurant(item, player)

game_board = Board()
ui = ConsoleUI()
players_list = game_start_routine()
while True:
    for current_player in players_list:
        if current_player.alive:
            game_step(current_player)