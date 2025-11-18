from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        self.deck = []

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.deck.append(Card(suit, rank))
    
    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        
        return "The deck has: " + deck_comp

