import random


class Player:
    def __init__(self, player_id, name, cash_initial=2000):
        self.player_id = player_id
        self.name = name
        self.cash = cash_initial
        self.position = 0
        self.job = None
        self.luck = 0
        self.backpack = []

    def move(self):
        steps = random.randint(1, 6)
        if self.position in [101,102]:
            #Start inside park
            if steps in [1,2,3,4]:
                #Stay inside park
                self.position = 101
            elif steps == 5:
                #Go to pond (inside park)
                self.position = 102
            elif steps == 6:
                #Exit park
                self.position = 31
        else:
            if self.position == 19 and steps != 6:
                #Will land inside branch road
                self.position += steps + 8 #Involves jumping from grid 19 to 28
            elif self.position in [28,29,30,31,32]:
                #Start inside branch road
                if self.position + steps >= 33:
                    #Will exit branch road
                    self.position = (self.position + steps - 8) % 28 #Involves jumping from grid 32 to 25
                else:
                    #Will stay inside branch road
                    self.position += steps
            else:
                self.position = (self.position + steps) % 28
        return steps, self.position

    def buy_ownable(self, target_ownable, has_level):
        if self.cash < target_ownable.price:
            return False
        else:
            self.cash -= target_ownable.price
            target_ownable.owner_id = self.player_id
            if has_level:
                target_ownable.level = 1
            return True

    def pay_rent_ownable(self, target_ownable, target_player):
        if self.cash < target_ownable.rent:
            return False
        else:
            self.cash -= target_ownable.rent
            target_player.cash += target_ownable.rent
            return True

    def upgrade_property(self, target_property):
        if target_property.level == 5:
            return 0
        elif self.cash < target_property.price:
            return -1
        else:
            self.cash -= target_property.price
            target_property.level += 1
            target_property.rent *= 2
            return 1

    def apply_for_job(self, target_job):
        if self.cash < target_job.application_cost:
            return -1
        else:
            self.cash -= target_job.application_cost
            l = self.luck / 100
            offer_rate = target_job.offer_rate * (1-l) + target_job.best_offer_rate * l
            if random.random() < offer_rate:
                self.job = target_job
                return 1
            else:
                return 0

    def receive_salary_if_applicable(self, target_tower):
        if self.job in target_tower.jobs:
            self.cash += self.job.salary
            return True
        else:
            return False

    def enter_park(self):
        self.position = 101
