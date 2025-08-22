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
    def __init__(self, title, application_cost, offer_rate, salary):
        self.title = title
        self.application_cost = application_cost
        self.offer_rate = offer_rate
        self.salary = salary


class Tower(Item):
    def __init__(self, name, jobs):
        super().__init__(name)
        self.jobs = jobs


class GoodChest(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO
    # 1% Legendary
    # 4% Epic
    # 10% Rare
    # 25% Uncommon
    # 60% Common


class BadChest(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO
    # 1% Legendarily Awful
    # 4% Epically Awful
    # 10% Rarely Awful
    # 25% Uncommonly Awful
    # 60% Commonly Awful


class Hotel(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Park(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Pond(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Bank(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Supermarket(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Restaurant(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


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
                    Job("Cashier", 120, 0.75, 60),
                    Job("Freelance Designer", 100, 0.2, 180),
                    Job("Store Manager", 600, 0.3, 360)
                ]
            ),
            "T2": Tower(
                name="Lasagna Tower",
                jobs=
                [
                    Job("IT Intern", 180, 0.6, 90),
                    Job("Software Engineer", 400, 0.35, 250),
                    Job("Senior Engineer", 800, 0.2, 500)
                ]
            ),
            "T3": Tower(
                name="Avocado Tower",
                jobs=
                [
                    Job("Bank Clerk", 300, 0.6, 100),
                    Job("Accountant", 500, 0.25, 360),
                    Job("Trader", 1000, 0.05, 1000)
                ]
            ),
            "T4": Tower(
                name="Burrito Tower",
                jobs=
                [
                    Job("Fine Artist", 50, 0.1, 225),
                    Job("Antique Collector", 700, 0.5, 225),
                    Job("Politician", 3000, 0.8, 375)
                ]
            )
        }
        self.good_chest = GoodChest("Chest")
        self.bad_chest = BadChest("Bad Chest")
        self.hotel = Hotel("Block No.7 Hotel")
        self.park = Park("City Park")
        self.pond = Pond("Mirror Pond")
        self.bank = Bank("Bank of Avocado")
        self.supermarket = Supermarket("Supermarket")
        self.restaurant = Restaurant("Object Oriented Restaurant")

        self.item_list = [
            [self.towers_dict["T4"], self.hotel],
            [self.properties_dict["A1"], self.hotel],
            [self.properties_dict["A2"], self.hotel],
            [self.good_chest, self.hotel],
            [self.pond],
            [self.properties_dict["A3"]],
            [self.properties_dict["B1"]],
            [self.bad_chest],
            [self.properties_dict["B1"]],
            [self.properties_dict["B2"]],
            [self.park],
            [self.properties_dict["C1"]],
            [self.properties_dict["C2"]],
            [self.supermarket],
            [self.good_chest, self.good_chest],
            [self.supermarket],
            [self.properties_dict["C3"]],
            [self.properties_dict["C4"]],
            [self.restaurant],
            [],
            [self.properties_dict["D1"]],
            [self.towers_dict["T1"], self.good_chest],
            [self.properties_dict["D1"], self.towers_dict["T1"]],
            [self.properties_dict["D2"], self.towers_dict["T2"]],
            [self.properties_dict["D3"], self.towers_dict["T2"]],
            [self.towers_dict["T3"]],
            [self.towers_dict["T3"], self.bank],
            [self.properties_dict["A1"], self.towers_dict["T4"]],
        ] # 2D List stating accessible items from a certain position

    def check_for_complete_group(self, letter, player):
        filtered_properties = [p for p in self.properties_dict.values() if p.group == letter]
        if all(p.owner_id == player.player_id for p in filtered_properties):
            for p in filtered_properties:
                p.rent *= 2
            return True
        else:
            return False