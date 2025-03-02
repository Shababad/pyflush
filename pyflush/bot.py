from .player import Player

class Bot(Player):
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

        self.configuration = {}