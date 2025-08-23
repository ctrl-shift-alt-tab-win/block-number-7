# noinspection PyMethodMayBeStatic
class ConsoleUIGame:
    def welcome(self):
        print("Welcome!")

    def enter_names(self):
        player1_name = input("Enter name of player 1: ")
        player2_name = input("Enter name of player 2: ")
        return player1_name, player2_name

    def turn_start_roll_dice(self, player):
        print(f"--------------{player.name}'s turn--------------")
        print(f"Your cash: {player.cash}")
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

    def alright_press_enter_continue(self):
        input("Alright. Press ENTER to continue.\n")

    def won(self, target_player):
        print(f"{target_player.name} WON!!!")
        input("Press ENTER to exit.\n")

    def feature_not_available(self):
        input("Feature currently not available. Press ENTER to continue.\n")


# noinspection PyMethodMayBeStatic
class ConsoleUIProperty:
    def ask_buy_property(self, item, player):
        print(f"No one owns {item.name}.")
        print(f"Your cash: {player.cash}")
        print(f"Cash needed to purchase {item.name}: {item.price}")
        choice = input(f"Would you like to buy {item.name}? (Y/N): ")
        return choice

    def buy_property_success(self, item, player):
        print(f"Successfully bought {item.name}!")
        print(f"The rent of {item.name} is currently {item.rent}")
        print(f"Your cash is now {player.cash}.")
        input("Press ENTER to continue.\n")

    def buy_property_failure(self, item):
        print(f"Not enough money to buy {item.name}...")
        input("Press ENTER to continue.\n")

    def ask_upgrade_property(self, item, player):
        print(f"You own {item.name}.")
        print(f"{item.name} is at level {item.level}.")
        print(f"Your cash: {player.cash}")
        print(f"Upgrade cost: {item.price}")
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

    def player_own_complete_group(self, letter):
        print(f"You now own all properties in group {letter}! Rent doubled.")
        input("Press ENTER to continue.\n")


# noinspection PyMethodMayBeStatic
class ConsoleUITower:
    def receive_salary(self, player, item):
        print(f"You received ${player.job.salary} salary as {player.job.title} in {item.name}!")
        print(f"Your cash: {player.cash}")
        input("Press ENTER to continue.\n")

    def ask_if_looking_for_jobs(self):
        choice = input(f"Are you currently looking for jobs? (Y/N): ")
        return choice

    def show_jobs_wait_application(self, player, item):
        print(f"Your cash: {player.cash}")
        i = 1
        for job in item.jobs:
            print(f"<PRESS {i} TO APPLY> | {job.title} | Application Cost: {job.application_cost} | Base Offer Rate: {job.offer_rate * 100}% | Salary: {job.salary}")
            i += 1
        print("<PRESS ANY OTHER KEY TO CANCEL>\n")
        print("Note: If you receive an offer, any previous job will be discarded.")
        choice = input("Please enter your choice: ")
        return choice

    def apply_job_failure_money(self, target_job):
        print(f"Not enough money to apply for {target_job.title}...")
        input("Press ENTER to continue.\n")

    def apply_job_failure_reject(self):
        print("Unfortunately, your application is rejected.")
        input("Press ENTER to continue.\n")

    def apply_job_success(self, player):
        print("Congratulations! Your application is accepted.")
        print(f"Your job: {player.job.title}")
        print(f"Your salary: {player.job.salary}")
        input("Press ENTER to continue.\n")


# noinspection PyMethodMayBeStatic
class ConsoleUIChest:
    def show_distribution_wait_draw_card(self, chest_type):
        if chest_type == "good":
            print("""
            |||||||||||||||||||||||||
            ||| BASE DISTRIBUTION |||
            |||                   |||
            ||| Legendary --- 1%  |||
            ||| Epic -------- 4%  |||
            ||| Rare -------- 10% |||
            ||| Uncommon ---- 25% |||
            ||| Common ------ 60% |||
            |||||||||||||||||||||||||
            """)
        elif chest_type == "bad":
            print("""
            |||||||||||||||||||||||||
            ||| BASE DISTRIBUTION |||
            |||                   |||
            ||| Awful++ ----- 1%  |||
            ||| Awful+ ------ 4%  |||
            ||| Awful ------- 10% |||
            ||| Mild -------- 25% |||
            ||| Minor ------- 60% |||
            |||||||||||||||||||||||||
            """)
        input("Press ENTER to draw a card from the chest!\n")

    def display_card(self, rarity, card):
        print(f"<<< ({rarity}) {card} >>>")

    def effect_claimed(self, chest_type):
        if chest_type == "good":
            print("Reward claimed!")
        elif chest_type == "bad":
            print("Punishment claimed.")
        input("Press ENTER to continue.\n")


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
