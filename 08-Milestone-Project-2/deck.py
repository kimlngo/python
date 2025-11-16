from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
