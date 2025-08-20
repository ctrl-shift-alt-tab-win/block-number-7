class ConsoleUIGame:
    def welcome(self):
        print("Welcome!")

    def enter_names(self):
        player1_name = input("Enter name of player 1: ")
        player2_name = input("Enter name of player 2: ")
        return player1_name, player2_name

    def turn_start_roll_dice(self, player):
        print(f"-------{player.name}'s turn-------")
        print(f"You are at position {player.position}.")
        input("Press ENTER to roll the dice!\n")

    def dice_landed(self, steps, position):
        print(f"The dice landed on {steps}!")
        print(f"Your current position is {position}!")
        input("Press ENTER to continue.\n")

    def show_accessible_items(self, accessible_items):
        print(f"You currently border:")
        for item in accessible_items:
            print(f"  {item.name}")
        input("Press ENTER to continue.\n")

    def consider_an_item(self, item):
        print(f"Considering {item.name}...")

    def won(self, target_player):
        print(f"{target_player.name} WON!!!")
        input("Press ENTER to exit.\n")

    def feature_not_available(self):
        input("Feature currently not available. Press ENTER to continue.\n")


class ConsoleUIProperty:
    def ask_buy_property(self, item, player):
        print(f"No one owns {item.name}.")
        print(f"Your cash: {player.cash}")
        print(f"Cash needed to purchase {item.name}: {item.price}")
        choice = input(f"Would you like to buy {item.name}? (Y/N): ")
        return choice

    def buy_property_success(self, item, player):
        print(f"Successfully bought {item.name}!")
        print(f"Your cash is now {player.cash}.")
        input("Press ENTER to continue.\n")

    def buy_property_failure(self, item):
        print(f"Not enough money to buy {item.name}...")
        input("Press ENTER to continue.\n")

    def player_refuse_buy_property(self):
        input("Alright. Press ENTER to continue.\n")

    def ask_upgrade_property(self, item):
        print(f"You own {item.name}.")
        print(f"{item.name} is at level {item.level}.")
        choice = input(f"Would you like to upgrade {item.name}? (Y/N): ")
        return choice

    def upgrade_property_success(self, item, player):
        print(f"Successfully upgraded {item.name}!")
        print(f"Your cash is now {player.cash}.")
        print(f"{item.name} is now at level {item.level} and the rent is now {item.rent}.")
        input("Press ENTER to continue.\n")

    def upgrade_property_failure_max_level(self, item):
        print(f"{item.name} is already at max level!")
        input("Press ENTER to continue.\n")

    def upgrade_property_failure_money(self, item):
        print(f"Not enough money to upgrade {item.name}...")
        input("Press ENTER to continue.\n")

    def player_refuse_upgrade_property(self):
        input("Alright. Press ENTER to continue.\n")

    def need_to_pay_rent(self, item, target_player):
        print(f"Oops, {item.name} is owned by {target_player.name}.")
        print(f"You need to pay rent of {item.rent}.")
        input("Press ENTER to pay rent.\n")

    def pay_rent_success(self, item, player, target_player):
        print(f"Successfully paid ${item.rent} for {item.name}...")
        print(f"Your cash is now {player.cash}.")
        print(f"{target_player.name}'s cash is now {target_player.cash}.")
        input("Press ENTER to continue.\n")

    def pay_rent_failure(self, item):
        print(f"Not enough money to pay rent for {item.name}...")





class ConsoleUITower:
    pass


class ConsoleUIChest:
    pass


class ConsoleUIHotel:
    pass


class ConsoleUIPark:
    pass


class ConsoleUIPond:
    pass


class ConsoleUIBank:
    pass


class ConsoleUISupermarket:
    pass


class ConsoleUIRestaurant:
    pass







class ConsoleUI:
    def __init__(self):
        self.game = ConsoleUIGame()
        self.property = ConsoleUIProperty()
        self.tower = ConsoleUITower()
        self.chest = ConsoleUIChest()
        self.hotel = ConsoleUIHotel()
        self.park = ConsoleUIPark()
        self.pond = ConsoleUIPond()
        self.bank = ConsoleUIBank()
        self.supermarket = ConsoleUISupermarket()
        self.restaurant = ConsoleUIRestaurant()
