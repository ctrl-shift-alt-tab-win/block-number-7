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
    player.move()
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
                    player.buy_property(item)
                else:
                    input("Alright. Press ENTER to continue.\n")
            elif item.owner_id == player.player_id:
                print(f"You own {item.name}.")
                print(f"{item.name} is at level {item.level}.")
                choice = input(f"Would you like to upgrade {item.name}? (Y/N): ")
                if choice == "Y":
                    player.upgrade_property(item)
                else:
                    input("Alright. Press ENTER to continue.\n")
            else:
                print(f"Oops, {item.name} is owned by {players_list[item.owner_id-1].name}.")
                print(f"You need to pay rent of {item.rent}.")
                input("Press ENTER to pay rent.\n")
                player.pay_rent(item, players_list[item.owner_id-1])

        elif isinstance(item, board.Chest):
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

        elif isinstance(item, board.Hotel):
            input("Feature currently not available. Press ENTER to continue.\n")
            #TODO


game_board = board.Board()
players_list = game_start_routine()
while True:
    for current_player in players_list:
        game_step(current_player)