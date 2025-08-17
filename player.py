import random
import sys


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
        input("Press ENTER to continue.\n")

    def buy_property(self, target_property):
        if self.cash < target_property.price:
            print(f"Not enough money to buy {target_property.name}...")
            input("Press ENTER to continue.\n")
        else:
            print(f"Successfully bought {target_property.name}!")
            self.cash -= target_property.price
            print(f"Your cash is now {self.cash}.")
            target_property.owner_id = self.player_id
            target_property.level = 1
            input("Press ENTER to continue.\n")

    def upgrade_property(self, target_property):
        if target_property.level == 3:
            print(f"{target_property.name} is already at max level!")
            input("Press ENTER to continue.\n")
        elif self.cash < target_property.price:
            print(f"Not enough money to upgrade {target_property.name}...")
            input("Press ENTER to continue.\n")
        else:
            print(f"Successfully upgraded {target_property.name}!")
            self.cash -= target_property.price
            print(f"Your cash is now {self.cash}.")
            target_property.level += 1
            target_property.rent *= 2
            print(f"{target_property.name} is now at level {target_property.level} and the rent is now {target_property.rent}.")
            input("Press ENTER to continue.\n")

    def pay_rent(self, target_property, target_player):
        if self.cash < target_property.rent:
            print(f"Not enough money to pay rent for {target_property.name}...")
            print(f"{target_player.name} WON!!!")
            input("Press ENTER to exit.\n")
            sys.exit()
            #TODO: Generalise to more than 2 players
        else:
            print(f"Successfully paid ${target_property.rent} for {target_property.name}...")
            self.cash -= target_property.rent
            target_player.cash += target_property.rent
            print(f"Your cash is now {self.cash}.")
            print(f"{target_player.name}'s cash is now {target_player.cash}.")
            input("Press ENTER to continue.\n")
