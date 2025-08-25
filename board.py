import random
from itertools import accumulate


class Item:
    def __init__(self, name):
        self.name = name


class Property(Item):
    def __init__(self, name, price, initial_rent, group, level=0, owner_id=0):
        super().__init__(name)
        self.price = price
        self.rent = initial_rent
        self.group = group
        self.level = level
        self.owner_id = owner_id


class Job:
    def __init__(self, title, application_cost, offer_rate, best_offer_rate, salary):
        self.title = title
        self.application_cost = application_cost
        self.offer_rate = offer_rate
        self.best_offer_rate = best_offer_rate
        self.salary = salary


class Tower(Item):
    def __init__(self, name, jobs):
        super().__init__(name)
        self.jobs = jobs


class Chest(Item):
    def __init__(self, name, base_dist, best_dist, rarity_dict, cards):
        super().__init__(name)
        self.base_dist = base_dist
        self.best_dist = best_dist
        self.rarity_dict = rarity_dict
        self.cards = cards

    def get_current_rarity_distribution(self, luck):
        l = luck / 100
        return [
            (1 - l) * base + l * best
            for base, best in zip(self.base_dist, self.best_dist)
        ]

    def draw_card(self, player):
        distribution = self.get_current_rarity_distribution(player.luck)
        boundaries = list(accumulate(distribution))
        r = random.random()
        for i in range(len(boundaries)):
            if r < boundaries[i]:
                return self.rarity_dict[i], random.choice(self.cards[i])
        return None

    def given_card_take_action(self, card, player, players_list, board):
        if card == "Cash x1.5":
            player.cash = int(player.cash * 1.5)
        elif card == "Every Owned Property Rent x1.5":
            for p in board.properties_dict.values():
                if p.owner_id == player.player_id:
                    p.rent = int(p.rent * 1.5)
        elif card == "Cash +400":
            player.cash += 400
        elif card == "Steal 7% From Every Other Player":
            for p in players_list:
                if p != player:
                    amount = int(p.cash * 0.07)
                    p.cash -= amount
                    player.cash += amount
        elif card == "Every Owned Property Rent x1.1":
            for p in board.properties_dict.values():
                if p.owner_id == player.player_id:
                    p.rent = int(p.rent * 1.1)
        elif card == "Cash +150":
            player.cash += 150
        elif card == "Luck +20":
            player.luck = min(player.luck+20, 100)
        elif card == "Steal 2% From Every Other Player":
            for p in players_list:
                if p != player:
                    amount = int(p.cash * 0.02)
                    p.cash -= amount
                    player.cash += amount
        elif card == "Standard Fishing Rod":
            player.backpack.append(FishingRod("Standard Fishing Rod", 2, 7))
        elif card == "Cash +70":
            player.cash += 70
        elif card == "Cash +50":
            player.cash += 50
        elif card == "Cash x1.02":
            player.cash = int(player.cash * 1.02)
        elif card == "Steal 1% From Every Other Player":
            for p in players_list:
                if p != player:
                    amount = int(p.cash * 0.01)
                    p.cash -= amount
                    player.cash += amount
        elif card == "Cash +20":
            player.cash += 20
        elif card == "Cash +10":
            player.cash += 10
        elif card == "Luck +2":
            player.luck = min(player.luck+2, 100)
        elif card == "Cash -50%":
            player.cash = int(player.cash * 0.5)
        elif card == "Every Owned Property Rent -33%":
            for p in board.properties_dict.values():
                if p.owner_id == player.player_id:
                    p.rent = int(p.rent * 0.67)
        elif card == "Reset Luck to 0":
            player.luck = 0
        elif card == "Clear Backpack":
            player.backpack = []
        elif card == "Cash -10%":
            player.cash = int(player.cash * 0.9)
        elif card == "Luck -50%":
            player.luck = int(player.luck * 0.5)
        elif card == "Cash -5%":
            player.cash = int(player.cash * 0.95)
        elif card == "Cash -4%":
            player.cash = int(player.cash * 0.96)
        elif card == "Cash -1%":
            player.cash = int(player.cash * 0.99)
        elif card == "Luck -5%":
            player.luck = int(player.luck * 0.95)


class GoodChest(Chest):
    def __init__(self, name):
        super().__init__(
            name,
            base_dist = [0.01, 0.04, 0.10, 0.25, 0.60],
            best_dist = [0.05, 0.10, 0.20, 0.30, 0.35],
            rarity_dict = {0:"Legendary", 1:"Epic", 2:"Rare", 3:"Uncommon", 4:"Common"},
            cards = [
                ["Cash x1.5", "Every Owned Property Rent x1.5"],
                ["Cash +400", "Steal 7% From Every Other Player", "Every Owned Property Rent x1.1"],
                ["Cash +150", "Luck +20", "Steal 2% From Every Other Player", "Standard Fishing Rod"],
                ["Cash +70", "Cash +50", "Cash x1.02", "Steal 1% From Every Other Player"],
                ["Cash +20", "Cash +10", "Luck +2"]
            ]
        )


class BadChest(Chest):
    def __init__(self, name):
        super().__init__(
            name,
            base_dist = [0.01, 0.04, 0.10, 0.25, 0.60],
            best_dist = [0.002, 0.008, 0.04, 0.25, 0.70],
            rarity_dict = {0: "Awful++", 1: "Awful+", 2: "Awful", 3: "Mild", 4: "Minor"},
            cards = [
                ["Cash -50%", "Every Owned Property Rent -33%"],
                ["Reset Luck to 0", "Clear Backpack"],
                ["Cash -10%", "Luck -50%"],
                ["Cash -5%", "Cash -4%"],
                ["Cash -1%", "Luck -5%"]
            ]
        )


class Park(Item):
    def __init__(self, name):
        super().__init__(name)
        self.price = 2000
        self.rent = 0
        self.owner_id = 0

    def increase_rent(self):
        self.rent += 20


class FishForSale:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class FishingRod:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health


class PondObject:
    def __init__(self, name, requirement, price_min, price_max, frequency, description):
        self.name = name
        self.requirement = requirement
        self.price_min = price_min
        self.price_max = price_max
        self.frequency = frequency
        self.description = description


class Pond(Item):
    def __init__(self, name):
        super().__init__(name)
        self.pond_object_list = [
            PondObject("Silver Minnow", 1, 1, 5, 50, "Tiny schooling fish, shiny scales."),
            PondObject("Spotted Pond Perch", 1, 10, 20, 50, "Small freshwater fish with green spots."),
            PondObject("Bluegill Sunfish", 1, 10, 30, 50, "Round, flat, and very common near ponds."),
            PondObject("River Catfish", 1, 10, 90, 30, "Whiskered bottom-dweller, always hungry."),
            PondObject("Rusty Crab", 1, 5, 10, 20, "Tiny, aggressive claws, easy to net."),
            PondObject("Glass Carp", 2, 5, 65, 80, "Nearly transparent body, eerie but beautiful."),
            PondObject("Speckled Tilapia", 2, 25, 35, 60, "Hardy farmed fish, mild taste."),
            PondObject("Spotted River Eel", 2, 40, 80, 40, "Slimy, slippery, wriggles out of nets."),
            PondObject("Red Claw Crayfish", 2, 15, 45, 40, "Small lobster-like creature, tasty claws."),
            PondObject("Painted Goby", 2, 15, 25, 20, "Tiny but brightly colored, like a rainbow."),
            PondObject("Dusky Pufferfish", 2, 40, 60, 20, "Inflates when startled, silly face."),
            PondObject("Rainbow Koi", 3, 40, 50, 100, "Decorative carp, shimmering patterns."),
            PondObject("Steelhead Salmon", 3, 100, 150, 50, "Muscular salmon, hard to reel in."),
            PondObject("Rock Lobster", 3, 50, 70, 40, "Large spiny lobster, strong shell."),
            PondObject("Electric Catfish", 3, 20, 40, 20, "Delivers mild shocks when handled."),
            PondObject("Velvet Stingray", 3, 120, 180, 10, "Flat, smooth body, hides in silt."),
            PondObject("Black Pike", 3, 100, 140, 5, "Long predator fish, sharp teeth."),
            PondObject("Orchid Betta", 4, 160, 170, 20, "Are you actually reading these descriptions?"),
            PondObject("River Otter", 4, 180, 240, 10, "It keeps stealing my bait."),
            PondObject("Great White Shark", 4, 200, 400, 10, "It's a relief that it was only going for my bait."),
            PondObject("Blue Whale", 4, 1000, 2000, 1, "I never knew this thing fits inside a pond.")
        ]

    def get_random_fish(self, player, fishing_rod):
        p = 0.5 + (player.luck / 200)
        fishing_rod.health -= 1
        if fishing_rod.health <= 0:
            player.backpack.remove(fishing_rod)
        if random.random() < p:
            objects = [x for x in self.pond_object_list if x.requirement <= fishing_rod.level]
            weights = [y.frequency for y in objects]
            fish = random.choices(population=objects, weights=weights, k=1)[0]
            price = random.randint(fish.price_min, fish.price_max)
            return fish.name, fish.description, price
        else:
            return None


class Bank(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Market(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Restaurant(Item):
    def __init__(self, name):
        super().__init__(name)
        self.food_names = ["Chicken Tikka Masala", "Spaghetti Bolognese", "Pepperoni Pasta Bake", "Special Fried Rice", "Sparkling Water"]
        self.food_prices = [69, 119, 149, 99, 99]
        self.food_chances = [0.7, 0.6, 0.5, 0.2, 1]
        self.food_luck_gains = [20, 40, 60, 100, None]

    def buy_food(self, option, player):
        price = self.food_prices[option-1]
        if player.cash < price:
            return -1
        else:
            player.cash -= price
            if random.random() < self.food_chances[option-1]:
                if option == 5:
                    player.luck = random.randint(0, 50)
                else:
                    player.luck = min(player.luck + self.food_luck_gains[option-1], 100)
                return 1
            else:
                return 0


class Board:
    def __init__(self):
        self.properties_dict = {
            "A1": Property(name="Aspen View 1", price=160, initial_rent=12, group="A"),
            "A2": Property(name="Aspen View 2", price=180, initial_rent=18, group="A"),
            "A3": Property(name="Aspen View 3", price=240, initial_rent=24, group="A"),
            "B1": Property(name="Birch Street 1", price=200, initial_rent=16, group="B"),
            "B2": Property(name="Birch Street 2", price=520, initial_rent=45, group="B"),
            "C1": Property(name="Cedar Heights 1", price=250, initial_rent=25, group="C"),
            "C2": Property(name="Cedar Heights 2", price=280, initial_rent=28, group="C"),
            "C3": Property(name="Cedar Heights 3", price=600, initial_rent=64, group="C"),
            "C4": Property(name="Cedar Heights 4", price=640, initial_rent=70, group="C"),
            "D1": Property(name="Downtown Plaza 1", price=1000, initial_rent=80, group="D"),
            "D2": Property(name="Downtown Plaza 2", price=1200, initial_rent=118, group="D"),
            "D3": Property(name="Downtown Plaza 3", price=1400, initial_rent=130, group="D"),
            "E1": Property(name="Emerald Estates 1", price=360, initial_rent=50, group="E"),
            "E2": Property(name="Emerald Estates 2", price=400, initial_rent=60, group="E"),
            "E3": Property(name="Emerald Estates 3", price=500, initial_rent=54, group="E")
        }
        self.towers_dict = {
            "T1": Tower(
                name="Falafel Tower",
                jobs=
                [
                    Job("Cashier", 120, 0.75, 0.9, 60),
                    Job("Freelance Designer", 100, 0.2, 0.25,180),
                    Job("Store Manager", 600, 0.3, 0.4,360)
                ]
            ),
            "T2": Tower(
                name="Lasagna Tower",
                jobs=
                [
                    Job("IT Intern", 180, 0.6, 0.8, 90),
                    Job("Software Engineer", 400, 0.35, 0.45, 250),
                    Job("Senior Engineer", 800, 0.2, 0.3, 500)
                ]
            ),
            "T3": Tower(
                name="Avocado Tower",
                jobs=
                [
                    Job("Bank Clerk", 300, 0.6, 0.75, 100),
                    Job("Accountant", 500, 0.25, 0.3, 360),
                    Job("Trader", 1000, 0.05, 0.07, 1000)
                ]
            ),
            "T4": Tower(
                name="Burrito Tower",
                jobs=
                [
                    Job("Fine Artist", 50, 0.1, 0.12, 140),
                    Job("Antique Collector", 700, 0.5, 0.6, 225),
                    Job("Politician", 3000, 0.8, 0.95, 375)
                ]
            )
        }
        self.good_chest = GoodChest("Chest")
        self.bad_chest = BadChest("Bad Chest")
        self.park = Park("City Park")
        self.pond = Pond("Object Oriented Pond")
        self.bank = Bank("Bank of Avocado")
        self.market = Market("Block No.7 Market")
        self.restaurant = Restaurant("Emerald Restaurant")

        self.item_list = [
            [self.towers_dict["T4"], self.good_chest],                  #0
            [self.properties_dict["A1"], self.bad_chest],               #1
            [self.properties_dict["A2"], self.good_chest],              #2
            [self.pond],                                                #3
            [self.pond],                                                #4
            [self.properties_dict["A3"]],                               #5
            [self.properties_dict["B1"]],                               #6
            [self.good_chest, self.good_chest],                         #7
            [self.properties_dict["B1"]],                               #8
            [self.properties_dict["B2"]],                               #9
            [self.park],                                                #10
            [self.properties_dict["C1"]],                               #11
            [self.properties_dict["C2"]],                               #12
            [self.market],                                              #13
            [self.bad_chest, self.bad_chest],                           #14
            [self.market],                                              #15
            [self.properties_dict["C3"]],                               #16
            [self.properties_dict["C4"]],                               #17
            [self.restaurant],                                          #18
            [self.bad_chest],                                           #19
            [self.properties_dict["D1"], self.good_chest],              #20
            [self.towers_dict["T1"], self.bad_chest],                   #21
            [self.properties_dict["D1"], self.towers_dict["T1"]],       #22
            [self.properties_dict["D2"], self.towers_dict["T2"]],       #23
            [self.properties_dict["D3"], self.towers_dict["T2"]],       #24
            [self.towers_dict["T3"]],                                   #25
            [self.towers_dict["T3"], self.bank],                        #26
            [self.properties_dict["A1"], self.towers_dict["T4"]],       #27
            [self.properties_dict["D1"], self.restaurant],              #28
            [self.properties_dict["D2"], self.properties_dict["E1"]],   #29
            [self.properties_dict["D3"], self.properties_dict["E2"]],   #30
            [self.properties_dict["E3"]],                               #31
            [self.properties_dict["D3"], self.bank]                     #32
        ] # 2D List stating accessible items from a certain position

    def check_for_complete_group(self, letter, player):
        filtered_properties = [p for p in self.properties_dict.values() if p.group == letter]
        if all(p.owner_id == player.player_id for p in filtered_properties):
            for p in filtered_properties:
                p.rent *= 2
            return True
        else:
            return False