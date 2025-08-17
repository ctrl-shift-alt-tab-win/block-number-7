class Item:
    def __init__(self, name):
        self.name = name


class Property(Item):
    def __init__(self, name, price, initial_rent, level, group, owner_id=0):
        super().__init__(name)
        self.price = price
        self.rent = initial_rent
        self.level = level
        self.group = group
        self.owner_id = owner_id


class Chest(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO
    # 1% Legendary
    # 4% Epic
    # 10% Rare
    # 25% Uncommon
    # 60% Common


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


class Hotel(Item):
    def __init__(self, name):
        super().__init__(name)
    #TODO


class Board:
    def __init__(self):
        self.property_a1 = Property(name="A1", price=100, initial_rent=10, level=0, group="A")
        self.property_a2 = Property(name="A2", price=120, initial_rent=12, level=0, group="A")
        self.property_a3 = Property(name="A3", price=150, initial_rent=16, level=0, group="A")
        self.property_b1 = Property(name="B1", price=200, initial_rent=15, level=0, group="B")
        self.property_b2 = Property(name="B2", price=240, initial_rent=30, level=0, group="B")
        self.property_c1 = Property(name="C1", price=280, initial_rent=27, level=0, group="C")
        self.property_c2 = Property(name="C2", price=300, initial_rent=30, level=0, group="C")
        self.property_c3 = Property(name="C3", price=360, initial_rent=38, level=0, group="C")
        self.property_c4 = Property(name="C4", price=400, initial_rent=40, level=0, group="C")
        self.property_d1 = Property(name="D1", price=420, initial_rent=42, level=0, group="D")
        self.property_d2 = Property(name="D2", price=500, initial_rent=50, level=0, group="D")
        self.property_d3 = Property(name="D3", price=540, initial_rent=54, level=0, group="D")
        self.property_e1 = Property(name="E1", price=600, initial_rent=60, level=0, group="E")
        self.property_e2 = Property(name="E2", price=800, initial_rent=80, level=0, group="E")
        self.property_e3 = Property(name="E3", price=1200, initial_rent=200, level=0, group="E")
        self.hotel = Hotel("Hotel")
        self.pond = Pond("Pond")
        self.supermarket = Supermarket("Supermarket")
        self.bank = Bank("Bank")
        self.chest = Chest("Chest")

        self.item_list = [
            [self.hotel],
            [self.property_a1, self.hotel],
            [self.property_a2, self.hotel],
            [self.chest, self.hotel],
            [self.property_e1, self.pond],
            [self.property_a3, self.property_e2],
            [self.property_b1, self.property_e3],
            [self.chest],
            [self.property_b1],
            [self.property_b2],
            [self.property_c1],
            [self.property_c2],
            [],
            [self.supermarket],
            [self.chest],
            [self.supermarket],
            [self.supermarket],
            [self.property_c3],
            [self.property_c4],
            [],
            [self.property_d1],
            [self.chest],
            [self.property_d1],
            [self.property_d2],
            [self.property_d3],
            [],
            [self.bank],
            [self.property_a1],
        ] # 2D List stating accessible items from a certain position
