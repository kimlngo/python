
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        
        #if total > 21 and still have ace
        #then change ace to be 1 instead of 11
        while self.value > 21 and self.aces: #(self.aces here use int as Truethy value like in JS)
            self.value -= 10
            self.aces -= 1
