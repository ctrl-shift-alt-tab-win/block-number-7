import sys

import board
from player import Player


def game_start_routine():
    print("Welcome!")
    player1_name = input("Enter name of player 1: ")
    player2_name = input("Enter name of player 2: ")
    players = [Player(1, player1_name), Player(2, player2_name)]
    return players


def game_step(player):
    print(f"-------{player.name}'s turn-------")
    print(f"You are at position {player.position}.")
    input("Press ENTER to roll the dice!\n")
    steps, position = player.move()
    print(f"The dice landed on {steps}!")
    print(f"Your current position is {position}!")
    input("Press ENTER to continue.\n")
    accessible_items = game_board.item_list[player.position]
    print(f"You currently border:")
    for item in accessible_items:
        print(f"  {item.name}")
    input("Press ENTER to continue.\n")
    for item in accessible_items:
        print(f"Considering {item.name}...")
        if isinstance(item, board.Property):
            if item.owner_id == 0:
                print(f"No one owns {item.name}.")
                print(f"Your cash: {player.cash}")
                print(f"Cash needed to purchase {item.name}: {item.price}")
                choice = input(f"Would you like to buy {item.name}? (Y/N): ")
                if choice == "Y":
                    if player.buy_property(item):
                        print(f"Successfully bought {item.name}!")
                        print(f"Your cash is now {player.cash}.")
                        input("Press ENTER to continue.\n")
                    else:
                        print(f"Not enough money to buy {item.name}...")
                        input("Press ENTER to continue.\n")
                else:
                    input("Alright. Press ENTER to continue.\n")
            elif item.owner_id == player.player_id:
                print(f"You own {item.name}.")
                print(f"{item.name} is at level {item.level}.")
                choice = input(f"Would you like to upgrade {item.name}? (Y/N): ")
                if choice == "Y":
                    status = player.upgrade_property(item)
                    if status == 1:
                        print(f"Successfully upgraded {item.name}!")
                        print(f"Your cash is now {player.cash}.")
                        print(f"{item.name} is now at level {item.level} and the rent is now {item.rent}.")
                        input("Press ENTER to continue.\n")
                    elif status == 0:
                        print(f"{item.name} is already at max level!")
                        input("Press ENTER to continue.\n")
                    elif status == -1:
                        print(f"Not enough money to upgrade {item.name}...")
                        input("Press ENTER to continue.\n")
                else:
                    input("Alright. Press ENTER to continue.\n")
            else:
                print(f"Oops, {item.name} is owned by {players_list[item.owner_id-1].name}.")
                print(f"You need to pay rent of {item.rent}.")
                input("Press ENTER to pay rent.\n")
                target_player = players_list[item.owner_id-1]
                if player.pay_rent(item, target_player):
                    print(f"Successfully paid ${item.rent} for {item.name}...")
                    print(f"Your cash is now {player.cash}.")
                    print(f"{target_player.name}'s cash is now {target_player.cash}.")
                    input("Press ENTER to continue.\n")
                else:
                    print(f"Not enough money to pay rent for {item.name}...")
                    print(f"{target_player.name} WON!!!")
                    input("Press ENTER to exit.\n")
                    sys.exit()
                    # TODO: Generalise to more than 2 players

        elif isinstance(item, board.Tower):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.GoodChest):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.BadChest):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Hotel):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Park):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Pond):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Bank):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Supermarket):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO

        elif isinstance(item, board.Restaurant):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO


game_board = board.Board()
players_list = game_start_routine()
while True:
    for current_player in players_list:
        game_step(current_player)