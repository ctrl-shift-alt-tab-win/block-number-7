class Player:
    def __init__(self, player_id, name, cash_initial=2000):
        self.player_id = player_id
        self.name = name
        self.cash = cash_initial
        self.position = 0
        self.property_list = []

    def move(self, steps):
        self.position = (self.position + steps) % 28