class Player:
    def __init__(self, player_id, name, cash_initial=2000):
        self.player_id = player_id
        self.name = name
        self.cash = cash_initial
        self.position = 0

    def move(self, steps):
        self.position = (self.position + steps) % 28

    def buy_property(self, target_property):
        if self.cash < target_property.price:
            print(f"Not enough money to buy {target_property.name}...")
        else:
            print(f"Successfully bought {target_property.name}!")
            self.cash -= target_property.price
            target_property.owner_id = self.player_id
            target_property.level = 1

    def upgrade_property(self, target_property):
        if target_property.level == 3:
            print(f"{target_property.name} is already at max level!")
        elif self.cash < target_property.price:
            print(f"Not enough money to upgrade {target_property.name}...")
        else:
            print(f"Successfully upgraded {target_property.name}!")
            self.cash -= target_property.price
            target_property.level += 1
            target_property.rent *= 2


