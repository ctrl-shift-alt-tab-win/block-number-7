import random


class Player:
    def __init__(self, player_id, name, cash_initial=2000):
        self.player_id = player_id
        self.name = name
        self.cash = cash_initial
        self.position = 0

    def move(self):
        steps = random.randint(1, 6)
        print(f"The dice landed on {steps}!")
        self.position = (self.position + steps) % 28
        print(f"Your current position is {self.position}!")

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

    def pay_rent(self, target_property, target_player):
        if self.cash < target_property.rent:
            print(f"Not enough money to pay rent for {target_property.name}...")
            print(f"{target_player.name} WON!!!")
            return False
            #TODO: Generalise to more than 2 players
        else:
            print(f"Successfully paid ${target_property.rent} for {target_property.name}...")
            self.cash -= target_property.rent
            target_player.rent += target_property.rent
            return True
