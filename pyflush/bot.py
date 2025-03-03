from .player import Player
from time import sleep

class Bot(Player):
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

        self.cards = []
        self.allin = False
        self.folded = False
        self.round_stake = 0
        self.total_stake = 0

        self.configuration = {}

    def bal(self, amount):
        self.balance += amount

    def stake(self, amount):
        self.round_stake += amount
        self.total_stake += amount

    def decide(self, bet, log) -> tuple[str, int | None]:
        if bet - self.round_stake:
            sleep(2)
            return "call", None
        else:
            sleep(2)
            return "check", None