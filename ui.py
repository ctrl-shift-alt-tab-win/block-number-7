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
        print(f"Your cash: ${player.cash}")
        if player.job is not None:
            print(f"Your job: {player.job.title}")
            print(f"Your salary: ${player.job.salary}")
        print(f"Your backpack: {len(player.backpack)}/{player.backpack_limit} items")
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

    def backpack_full(self):
        print("Sorry, your backpack is full.")
        input("Press ENTER to continue.\n")

    def ask_if_use_controllable_dice(self, player):
        print(f"You have {player.backpack.count("Controllable Dice")} controllable dice.")
        choice = input("Do you want to use one? (Y/N): ")
        return choice

    def wait_integer_1_6(self):
        print("Alright!")
        number = input("Please enter an integer between 1 and 6: ")
        return number

    def not_enter_integer_1_6(self):
        print("Sorry, you didn't enter an integer between 1 and 6.")
        print("Normal dice will be used.")
        input("Press ENTER to continue.\n")

    def alright_press_enter_continue(self):
        input("Alright. Press ENTER to continue.\n")

    def won(self, target_player):
        print(f"{target_player.name} WON!!!")
        input("Press ENTER to exit.\n")

    def feature_not_available(self):
        input("Feature currently not available. Press ENTER to continue.\n")


class ConsoleUIOwnable:
    def ask_if_buy(self, item, player):
        print(f"No one owns {item.name}.")
        print(f"Your cash: ${player.cash}")
        print(f"Cash needed to purchase {item.name}: ${item.price}")
        choice = input(f"Would you like to buy {item.name}? (Y/N): ")
        return choice

    def buy_success(self, item, player):
        print(f"Successfully bought {item.name}!")
        print(f"The rent of {item.name} is currently ${item.rent}.")
        print(f"Your cash is now ${player.cash}.")
        input("Press ENTER to continue.\n")

    def buy_failure(self, item):
        print(f"Not enough money to buy {item.name}...")
        input("Press ENTER to continue.\n")

    def need_to_pay_rent(self, item, target_player):
        print(f"Oops, {item.name} is owned by {target_player.name}.")
        print(f"You need to pay the rent of ${item.rent}.")
        input("Press ENTER to pay the rent.\n")

    def pay_rent_success(self, item, player, target_player):
        print(f"Successfully paid ${item.rent} for {item.name}...")
        print(f"Your cash is now ${player.cash}.")
        print(f"{target_player.name}'s cash is now ${target_player.cash}.")
        input("Press ENTER to continue.\n")

    def pay_rent_failure(self, item):
        print(f"Not enough money to pay rent for {item.name}...")


# noinspection PyMethodMayBeStatic
class ConsoleUIProperty:
    def ask_upgrade_property(self, item, player):
        print(f"You own {item.name}.")
        print(f"{item.name} is at level {item.level}.")
        print(f"Your cash: ${player.cash}")
        print(f"Upgrade cost: ${item.price}")
        choice = input(f"Would you like to upgrade {item.name}? (Y/N): ")
        return choice

    def upgrade_property_success(self, item, player):
        print(f"Successfully upgraded {item.name}!")
        print(f"Your cash is now ${player.cash}.")
        print(f"{item.name} is now at level {item.level} and the rent is now ${item.rent}.")
        input("Press ENTER to continue.\n")

    def upgrade_property_failure_max_level(self, item):
        print(f"{item.name} is already at max level!")
        input("Press ENTER to continue.\n")

    def upgrade_property_failure_money(self, item):
        print(f"Not enough money to upgrade {item.name}...")
        input("Press ENTER to continue.\n")

    def player_own_complete_group(self, letter):
        print(f"You now own all properties in group {letter}! Rent doubled.")
        input("Press ENTER to continue.\n")


# noinspection PyMethodMayBeStatic
class ConsoleUITower:
    def receive_salary(self, player, item):
        print(f"You received ${player.job.salary} salary as {player.job.title} in {item.name}!")
        print(f"Your cash: ${player.cash}")
        input("Press ENTER to continue.\n")

    def ask_if_looking_for_jobs(self):
        choice = input(f"Are you currently looking for jobs? (Y/N): ")
        return choice

    def show_jobs_wait_application(self, player, item):
        print(f"Your cash: ${player.cash}")
        i = 1
        for job in item.jobs:
            print(f"<PRESS {i} TO APPLY> | {job.title} | Application Cost: ${job.application_cost} | Base Offer Rate: {job.offer_rate * 100}% | Salary: ${job.salary}")
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
        print(f"Your salary: ${player.job.salary}")
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

    def awful_luck_shield_activated(self, player):
        print("Awful luck shield activated!")
        print(f"You have {player.backpack.count("Awful Luck Shield")} awful luck shield left.")
        input("Press ENTER to continue.\n")


class ConsoleUIPark:
    def stuck_in_park_increase_rent(self):
        print("You are stuck inside the park, but the park's rent just increased by $20!")
        input("Press ENTER to continue.\n")

    def stuck_in_park_access_pond(self):
        print("You are stuck inside the park, but you now have access to the pond!")

    def own_park_ask_if_enter(self):
        print("You own this park.")
        choice = input("Do you want to enter the park? (Y/N): ")
        return choice

    def now_inside_park(self):
        print("You are now inside the park.")
        input("Press ENTER to continue.\n")


class ConsoleUIPond:
    def show_fishing_rods_wait_choice(self, fishing_rods_in_backpack):
        print("Your fishing rods: ")
        i = 1
        for fishing_rod in fishing_rods_in_backpack:
            print(f"<PRESS {i} TO USE THIS FISHING ROD> | {fishing_rod.name} | Health Remaining: {fishing_rod.health}")
            i += 1
        print("<PRESS ANY OTHER KEY TO CANCEL>\n")
        choice_number = input("Please enter your choice: ")
        return choice_number, (i-1)

    def show_fish_caught(self, name, description, price, rarity):
        print(f"You caught something... ")
        input("Press ENTER to reveal!\n")
        print(f"*** ({rarity}) {name} ***")
        print(f"\"{description}\"")
        print(f"Can be sold for: ${price}\n")
        input("Press ENTER to continue.\n")

    def catch_nothing(self):
        print("You didn't catch anything...")
        input("Press ENTER to continue.\n")

    def no_fishing_rod(self):
        print("You don't have any fishing rod.")
        input("Press ENTER to continue.\n")

    def ask_if_use_glowing_bait(self, player):
        print(f"You have {player.backpack.count("Glowing Bait")} glowing bait.")
        choice = input("Do you want to use one? (Y/N): ")
        return choice

    def attached_glowing_bait(self):
        print("Successfully attached glowing bait.")
        input("Press ENTER to continue.\n")


class ConsoleUIBank:
    pass


class ConsoleUIMarket:
    def show_option_buy_sell_wait_choice(self):
        print("<PRESS 1 TO BUY>")
        print("<PRESS 2 TO SELL>")
        print("<PRESS ANY OTHER KEY TO CANCEL>\n")
        choice_number = input("Please enter your choice: ")
        return choice_number

    def show_market_buy_wait_choice(self, player):
        print(f"<<< MARKET (BUYING) >>>")
        print(f"<PRESS 1> | 1x Makeshift Fishing Rod | $59  | Can fish 3 times, accessing easy fish                              | Remaining Purchases: {player.limit_dict["Makeshift Fishing Rod"]}")
        print(f"<PRESS 2> | 1x Standard Fishing Rod  | $159 | Can fish 5 times, accessing easy & medium fish                     | Remaining Purchases: {player.limit_dict["Standard Fishing Rod"]}")
        print(f"<PRESS 3> | 1x Fine Fishing Rod      | $319 | Can fish 7 times, accessing easy & medium & hard fish              | Remaining Purchases: {player.limit_dict["Fine Fishing Rod"]}")
        print(f"<PRESS 4> | 1x Golden Fishing Rod    | $599 | Can fish 9 times, accessing easy & medium & hard & impossible fish | Remaining Purchases: {player.limit_dict["Golden Fishing Rod"]}")
        print(f"<PRESS 5> | 1x Glowing Bait          | $39  | Can only attach to golden rod, guarantees hard & impossible fish   | Remaining Purchases: {player.limit_dict["Glowing Bait"]}")
        print(f"<PRESS 6> | 1x Controllable Dice     | $119 | Allows you to control your dice rolling outcome for one time       | Remaining Purchases: {player.limit_dict["Controllable Dice"]}")
        print(f"<PRESS 7> | 1x Awful Luck Shield     | $199 | Exempted once if getting an Awful/Awful+/Awful++ from bad chest    | Remaining Purchases: {player.limit_dict["Awful Luck Shield"]}")
        print(f"<PRESS 8> | Backpack Upgrade         | $400 | Double the space of your backpack (4 items -> 8 items -> 16 items) | Remaining Purchases: {player.limit_dict["Backpack Upgrade"]}")
        print(f"<PRESS ANY OTHER KEY TO CANCEL>\n")
        print(f"Note: You can buy at most one item at a time.")
        choice_number_inner = input("Please enter your choice: ")
        return choice_number_inner

    def max_purchase_limit_reached(self):
        print("Sorry, maximum purchase limit already reached.")
        input("Press ENTER to continue.\n")

    def not_enough_money_buy_item(self):
        print(f"Not enough money to buy this item...")
        input("Press ENTER to continue.\n")

    def purchase_success_item_added_backpack(self):
        print("Successfully purchased!")
        print("The item is added to your backpack.")
        input("Press ENTER to continue.\n")

    def purchase_success_backpack_upgraded(self, player):
        print("Successfully purchased!")
        print(f"Your backpack space is now {player.backpack_limit}.")
        input("Press ENTER to continue.\n")

    def no_sellable_item(self):
        print("Sorry, none of the items in your backpack can be sold.")
        input("Press ENTER to continue.\n")

    def show_market_selling_title(self):
        print("<<< MARKET (SELLING) >>>")

    def sell_item_wait_choice(self, thing):
        print(f"{thing.name} | Can be sold for: ${thing.price}")
        choice = input("Do you want to sell this item? (Y/N): ")
        return choice

    def sold_success(self):
        print("Successfully sold!")
        input("Press ENTER to continue.\n")


class ConsoleUIRestaurant:
    def show_menu_wait_choice(self, player):
        print("<<< MENU >>>")
        print("<PRESS 1 TO SELECT> | Chicken Tikka Masala | $69  | 70% Chance to Gain 20 Luck")
        print("<PRESS 2 TO SELECT> | Spaghetti Bolognese  | $119 | 60% Chance to Gain 40 Luck")
        print("<PRESS 3 TO SELECT> | Pepperoni Pasta Bake | $149 | 50% Chance to Gain 60 Luck")
        print("<PRESS 4 TO SELECT> | Special Fried Rice   | $99  | 20% Chance to Gain 100 Luck")
        print("<PRESS 5 TO SELECT> | Sparkling Water      | $99  | Set Luck to a Random Value Between 0 and 50")
        print("<PRESS ANY OTHER KEY TO CANCEL>\n")
        print(f"Your current luck: {player.luck}")
        choice_number = input("Please enter your choice: ")
        return choice_number

    def buy_food_success_gain_luck(self, player):
        print(f"Success! Your luck is now {player.luck}.")
        input("Press ENTER to continue.\n")

    def buy_food_success_not_gain_luck(self):
        print("Sadly, there's no changes to your luck...")
        input("Press ENTER to continue.\n")

    def buy_food_failure_money(self):
        print(f"Not enough money to buy this food.")
        input("Press ENTER to continue.\n")


class ConsoleUI:
    def __init__(self):
        self.game = ConsoleUIGame()
        self.ownable = ConsoleUIOwnable()
        self.property = ConsoleUIProperty()
        self.tower = ConsoleUITower()
        self.chest = ConsoleUIChest()
        self.park = ConsoleUIPark()
        self.pond = ConsoleUIPond()
        self.bank = ConsoleUIBank()
        self.market = ConsoleUIMarket()
        self.restaurant = ConsoleUIRestaurant()
