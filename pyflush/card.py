values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
suits = {"S": "♠", "C": "♣", "H": "♥", "D": "♦"} # Spades, Clubs, Hearts, Diamonds

class Card():
    def __init__(self, rank: str, suit: str):
        """
        rank: str, e.g. "5" or "T"
        suit: str, e.g. "S" or "D"
        """
        self.rank = rank
        self.suit = suit

        self.value = values[rank]
        self.name = f"{self.rank}{suits[self.suit]}"

    def __str__(self):
        return f"{self.rank}{suits[self.suit]}"