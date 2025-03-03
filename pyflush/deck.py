from .card import Card
from random import randint, shuffle as shuffle_

rank_list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suit_list = ["S", "C", "H", "D"]

class Deck():
    def __init__(self):
        """
        Deck of playing cards
        Methods:
        draw(), draws a card from the deck
        shuffle(), shuffles the cards in the deck
        collect(), collects every card that has been drawn out the deck
        """
        self.deck = [Card(rank, suit) for suit in suit_list for rank in rank_list]
        self.used = []

    def draw(self) -> Card:
        """
        Draws a card from the deck
        """
        if len(self.used) == len(self.deck):
            raise Exception("No cards in deck!")

        card = self.deck[randint(0,51)]
        while card in self.used:
            card = self.deck[randint(0,51)]
        
        self.used.append(card)
        
        return card
        
    def shuffle(self) -> None:
        """
        Shuffle the cards in the deck
        """
        shuffle_(self.deck)

    def collect(self) -> None:
        """
        Collect every card that has been drawn out the deck
        """
        self.used = []

    def __iter__(self):
        return iter(self.deck)