from card import Card

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            #cannot use append here because it will
            #add a whole list of cards into the self.all_cards
            #e.g., ['A', 'B', ['C', 'D']]
            self.all_cards.extend(new_cards)
        else:
            #for single card
            self.all_cards.append(new_cards)
    
    def is_out_of_cards(self):
        return len(self.all_cards) == 0

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    