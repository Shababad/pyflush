from .player import Player
from .bot import Bot
from .deck import Deck

class Game():
    def __init__(self):
        self.deck: list = Deck()
        self.players: list = []
        self.blind: int = None
        self.print_status: bool = True

    # LOCAL CLASS FUNCTIONS #
    def pr(self, content) -> None:
        if self.print_status:
            print(content)

    # CLASS METHODS
    def toggle_print(self):
        if self.print_status is True:
            self.print_status = False
        else:
            self.print_status = True
        if self.print_status is True:
            print("Printing configuration process turned on!")
        else:
            print("Printing configuration process turned off!")

    def add_player(self, name: str, balance: int) -> None:
        """
        Add a player to the game
        """
        if name in [p.name for p in self.players]:
            raise Exception(f"Player with name: '{name}' already exists!")
        else:
            player = Player(name, balance)
            self.players.append(player)
            self.pr(f"Player '{name}' added to the game!")
            

    def add_bot(self, name: str, balance: int) -> None:
        """
        Add a bot to the game
        """
        if name in [p.name for p in self.players]:
            raise Exception(f"Bot with name: '{name}' already exists!")
        else:
            player = Bot(name, balance)
            self.players.append(player)
            self.pr(f"Bot '{name}' added to the game!")

    def remove(self, name) -> None:
        """
        Remove a player/bot from the game
        """
        player = None
        for p in self.players:
            if p.name == name:
                player = p
        if player == None:
            raise Exception(f"No player/bot named '{name}' was found!")
        else: 
            self.players.remove(player)
            self.pr(f"Player/Bot '{name}' removed from the game!")

    def set_blind(self, blind: int):
        """
        Sets big blind, must be integer, even num, greater than 1
        """
        if blind < 2:
            raise Exception("Blind minimum is 2")
        elif blind % 2:
            raise Exception("Blind must be even")
        else:
            self.blind = blind
            self.pr(f"Blind set to {int(blind/2)}/{blind}")

    def start_round():
        pass