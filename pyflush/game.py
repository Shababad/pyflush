from .player import Player
from .bot import Bot
from .deck import Deck
from time import sleep
from tqdm import tqdm

class Game():
    def __init__(self, blind: int = None, print_status: bool = True):

        self.blind: int = blind
        self.print_status: bool = print_status

        self.deck: list = Deck()
        self.players: list[Player] = []
        self.com_cards = []
        self.pot = 0
        self.btn = 0
        self.log = {}
        self.wait_time = 1

    # ---------- LOCAL ACTION FUNCTIONS ---------- #
    
    def pr(self, content) -> None:
        if self.print_status:
            print(content)

    def process_action(self, player, action_tuple, bet):
        round_stake = player.round_stake
        action = action_tuple[0]
        amount = action_tuple[1]
        if action == "check":
            return f"{player.name} ({player.balance}) checks."
        
        elif action == "fold":
            player.folded = True
            return f"{player.name} ({player.balance}) folds."
        
        elif action == "all_in":
            all_in_value = player.balance
            player.allin = True
            player.balance = 0
            return f"{player.name} ({player.balance}) goes all in with {all_in_value} (+{bet-round_stake})."
        
        elif action == "call":
            player.bal(-(bet - round_stake))
            player.round_stake += (bet - round_stake)
            return f"{player.name} ({player.balance}) calls {bet} (+{bet-round_stake})."
        
        elif action == "bet":
            player.bal(-(bet - round_stake))
            player.round_stake += (bet - round_stake)
            return f"{player.name} ({player.balance}) bets {amount} (+{bet-round_stake})."
        
        elif action == "raise":
            player.bal(-(bet - round_stake))
            player.round_stake += (bet - round_stake)
            return f"{player.name} ({player.balance}) raises to {amount} (+{bet-round_stake})."
        
    def reset_new_round(self):
        for p in self.players:
            p.round_stake = 0

    def process_blinds(self):
        num_players = len(self.players)
        blind = self.blind
        self.btn += 1
        btn = self.players[self.btn % num_players]
        sb = self.players[(self.btn + 1) % num_players]
        bb = self.players[(self.btn + 2) % num_players]

        # Check if sb and bb have required balance
        if sb.balance < blind / 2:
            self.all_in_(sb)
        else:
            sb.bal(-(blind / 2))
            sb.stake((blind / 2))

        if bb.balance < blind:
            self.all_in_(bb)
        else:
            bb.bal(-blind)
            bb.stake(blind)

        print(f"Dealer: {btn.name}")
        print(f"Big blind: {bb.name}")
        print(f"Small blind: {sb.name}")

    def round(self):

        num_players = len(self.players)
        bet: int = 0
        i = (self.btn + 1) % num_players
        turn = self.players[i]
        count = 0
        last_raiser = None

        # If preflop
        if len(self.com_cards) == 0:
            bet = self.blind
            i = (self.btn + 3) % num_players
        
        while count < num_players:
            turn = self.players[i]
            if len([p for p in self.players if not p.folded]) < 2:
                pass # Game instantly ends and player who didnt fold wins
            if len([p for p in self.players if not p.allin]) < 2:
                pass # Open until river card without betting rounds

            if turn.folded or turn.allin:
                turn += 1
                count += 1
                continue

            if i == last_raiser:
                break
            
            print(f"{turn.name}'s turn: ")

            action = turn.decide(bet, self.log)
            if action[1] is not None:
                bet = action[1]
                count = 1
                last_raiser = i
            else:
                count += 1
            print(self.process_action(turn, action, bet))
            print("-" * 30)
            i = (i + 1) % num_players

    # ---------- GLOBAL MODULE METHODS ---------- #

    def toggle_print(self):
        """
        Toggles configuration process printing
        """
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
        # If the input name already exists
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
        # If the input name already exists
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

    def start(self):
        """
        Starts an automatic game with current players
        """
        def br():
            print("="*60)
        if len(self.players) < 2:
            raise Exception("Not enough players in game! Must be at least 2.")
        
        if self.blind is None:
            raise Exception("Blind should not be None!")
        
        if len([p for p in self.players if p.balance > 0]) < 2:
            raise Exception("At least 2 player must have a balance greater than 0!")
        
        self.deck.shuffle()
        self.process_blinds()

        # Give every player hole cards
        for i in range(2):
            for p in self.players:
                if not p.balance == 0:
                    p.cards.append(self.deck.draw())

        print([card.name for card in self.deck.used])
        br()

        # Preflop round
        print("POKER GAME")
        print(f"Players: {[p.name for p in self.players]}")
        for i in tqdm (range (len(self.players) * 2), desc="Dealing cards..."):
            sleep(0.1)
        br()
        self.round()
        self.reset_new_round()
        br()

        # Flop round
        print("FLOP CARDS")
        for i in range(3):
            self.com_cards.append(self.deck.draw())
        print(f"Community Cards: {[card.name for card in self.com_cards]}")
        br()
        self.round()
        self.reset_new_round()
        br()

        # Turn round
        print("TURN CARD")
        self.com_cards.append(self.deck.draw())
        print(f"Community Cards: {[card.name for card in self.com_cards]}")
        br()
        self.round()
        self.reset_new_round()
        br()

        # River round
        print("RIVER CARD")
        self.com_cards.append(self.deck.draw())
        print(f"Community Cards: {[card.name for card in self.com_cards]}")
        br()
        self.round()