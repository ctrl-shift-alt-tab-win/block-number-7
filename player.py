import random


class Player:
    def __init__(self, player_id, name, cash_initial=2000):
        self.player_id = player_id
        self.name = name
        self.cash = cash_initial
        self.position = 0
        self.job = None

    def move(self):
        steps = random.randint(1, 6)
        self.position = (self.position + steps) % 28
        return steps, self.position

    def buy_property(self, target_property):
        if self.cash < target_property.price:
            return False
        else:
            self.cash -= target_property.price
            target_property.owner_id = self.player_id
            target_property.level = 1
            return True

    def upgrade_property(self, target_property):
        if target_property.level == 3:
            return 0
        elif self.cash < target_property.price:
            return -1
        else:
            self.cash -= target_property.price
            target_property.level += 1
            target_property.rent *= 2
            return 1

    def pay_rent(self, target_property, target_player):
        if self.cash < target_property.rent:
            return False
        else:
            self.cash -= target_property.rent
            target_player.cash += target_property.rent
            return True

    def apply_for_job(self, target_job):
        if self.cash < target_job.application_cost:
            return -1
        else:
            self.cash -= target_job.application_cost
            if random.random() < target_job.offer_rate:
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
