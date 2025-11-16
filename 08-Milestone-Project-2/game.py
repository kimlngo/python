from deck import Deck
from player import Player

#Game setup
DRAW_THRESHOLD = 5
playerOne = Player('One')
playerTwo = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    playerOne.add_cards(new_deck.deal_one())
    playerTwo.add_cards(new_deck.deal_one())

#Game Logic
game_on = True

round_number = 0

while game_on:
    round_number +=1
    print(f'Round {round_number}')

    if playerOne.is_out_of_cards():
        print('Player One, out of cards.')
        print('Player TWO wins')
        game_on = False
        break
    if playerTwo.is_out_of_cards():
        print('Player Two, out of cards.')
        print('Player ONE wins')
        game_on = False
        break

    #Start a new round
    player_one_cards = []
    player_one_cards.append(playerOne.remove_one())

    player_two_cards = []
    player_two_cards.append(playerTwo.remove_one())

    #while at-war
    at_war = True

    while at_war:
        p1_card_val = player_one_cards[-1].value
        p2_card_val = player_two_cards[-1].value

        if p1_card_val > p2_card_val:
            playerOne.add_cards(player_one_cards)
            playerOne.add_cards(player_two_cards)
            at_war = False
        elif p1_card_val < p2_card_val:
            playerTwo.add_cards(player_one_cards)
            playerTwo.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!!!')

            if len(playerOne.all_cards) < DRAW_THRESHOLD:
                print(f'Player One has {len(playerOne.all_cards)} cards and unable to declare war')
                print('Player TWO wins')
                game_on = False
                break

            elif len(playerTwo.all_cards) < DRAW_THRESHOLD:
                print(f'Player Two has {len(playerTwo.all_cards)} cards and unable to declare war')
                print('Player ONE wins')
                game_on = False
                break
            else:
                for _ in range(DRAW_THRESHOLD):
                    player_one_cards.append(playerOne.remove_one())
                    player_two_cards.append(playerTwo.remove_one())