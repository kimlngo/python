from chip import Chip
from hand import Hand
from deck import Deck

playing = True

def take_bet(chip):
    cont_asking = True

    while cont_asking:
        try:
            bet_input = int(input(f'Please enter your bet between 1 and {chip.total}: '))

            if bet_input < 1:
                print(f"Please enter bet amount between 1 and {chip.total}")
            elif bet_input <= chip.total:
                chip.bet = bet_input
                cont_asking = False
            else:
                print("Sorry, you do not have enough chips, please enter another amount")
        except:
            print("Sorry, that's not a valid bet, please try again")


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        hit_stand = input('Hit or Stand? Enter h or s: ')

        if hit_stand[0].lower() == 'h':
            hit(deck, hand)

        elif hit_stand[0].lower() == 's':
            print("Player stands - Dealer's Turn")
            playing = False
        else:
            print("Sorry, invalid input, please enter h or s only")
            continue
        break

def show_some_cards(player, dealer):
    # show one card of the dealer
    print("\nDealer's Hand: ")
    print("First card is hidden")
    print(dealer.cards[1]) # card[0] is hidden

    # show two cards of the player
    print("\nPlayer's Hand: ", *player.cards, sep='\n')

def show_all_cards(player, dealer):
    print("\nDealer's Hand - All Cards: ", *dealer.cards, sep='\n')
    print(f"\nDealer's card values: {dealer.value}")

    print("\nPlayer's Hand - All Cards: ", *player.cards, sep='\n')
    print(f"\nPlayer's card values: {player.value}")

def player_busts(player, dealer, chip):
    print('BUST PLAYER!')
    chip.lose_bet()
    pass

def player_wins(player, dealer, chip):
    print('PLAYER WINS!')
    chip.win_bet()
    pass

def dealer_busts(player, dealer, chip):
    print('PLAYER WINS! DEALER BUSTED')
    chip.win_bet()

def dealer_wins(player, dealer, chip):
    print('DEALER WINS!')
    chip.lose_bet()
    pass

def push(player, dealer, chip):
    print('Dealer and player tied! PUSH')


while True:

    #1 create & shuffle a deck
    deck = Deck()
    deck.shuffle()

    #2 create two hands, one for player and one for dealer
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    #3 setup player's chip
    player_chips = Chip()
    take_bet(player_chips)

    #4 show cards initially
    show_some_cards(player, dealer)

    while playing:
        # prompt hit or stand
        hit_or_stand(deck, player)

        # show some cards
        show_some_cards(player, dealer)

        # if player's hand value > 21 --> player busted
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.value <= 21:
        while dealer.value < 17: #soft value 17
            hit(deck, dealer)
        
        #show all cards
        show_all_cards(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)
        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)
        else:
            push(player, dealer, player_chips)


    print(f"\nPlayer total chips: {player_chips.total}")

    # Ask for continue playing
    new_game = input("Would you like to play again? (y or n): ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")
        break
