import random

game_board = []
mark_x = 'X'
mark_o = 'O'
acceptable_range = range(1, 10)
index_dict = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2)}
player_turn = {}
player_first = ''
player_second = ''
PLAYER_ONE = 'Player 1'
PLAYER_TWO = 'Player 2'
used_numbers = []

def init():
    global game_board, player_turn, player_first, player_second, used_numbers
    game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    player_first = ''
    player_second = ''
    player_turn = {}
    used_numbers = []

def display_game_board():
    for i, row in enumerate(game_board):
        print(f"\t {row[0]} | {row[1]} | {row[2]} ")
        if i != len(game_board) - 1:
            print("\t-----------")

def set_marker(number, value):
    row, col = index_dict[number]
    game_board[row][col] = value

def pick_marker():
    choice = ''

    while choice.upper() not in ['X', 'O']:
        choice = input('Please pick a marker X or O: ')

    return choice.upper()

def set_player_turn(marker):
    '''use randomint function to randomly choose who play first
    0 - player 1 go first
    1 - player 2 go first
    '''
    random_num = random.randint(0,1)
    if random_num == 0:
        player_first = PLAYER_ONE
        player_second = PLAYER_TWO
    else:
        player_first = PLAYER_TWO
        player_second = PLAYER_ONE

    player_turn[mark_x] = player_first
    player_turn[mark_o] = player_second

    print(f'\t{player_turn[mark_x]} (X) go First')
    print(f'\t{player_turn[mark_o]} (O) go Second')

def get_number():
    number = ''
    within_range = False
    is_picked = False

    while not (number.isdigit() and within_range and not is_picked):
        number = input('Please pick a number: ')

        if not number.isdigit:
            print('Sorry, this is not a number')
        elif not int(number) in acceptable_range:
            print('Sorry, this number is not in range 1 - 9')
        elif number in used_numbers:
            print('Sorry, this number is already picked')
            is_picked = True
        else:
            within_range = True
            is_picked = False

    return number

def check_winner(marker):
    '''check if a player (marker) has won:
    @input: marker (X or O)
    @output:
        - "Player 1"
        - "Player 2"
        - None
    '''
    win_pattern = [marker] * 3
    
    #check all horizons
    if win_pattern in [game_board[0], game_board[1], game_board[2]]:
        return player_turn[marker]
    
    #check all verticals
    for col in range(0, 3):
        column  = []
        for row in range(0, 3):
            column.append(game_board[row][col])
        
        if column == win_pattern:
            return player_turn[marker]

    #check all diagonals
    diagonal_1 = [game_board[0][0], game_board[1][1], game_board[2][2]]
    diagonal_2 = [game_board[2][0], game_board[1][1], game_board[0][2]]

    if win_pattern in [diagonal_1, diagonal_2]:
        return player_turn[marker]

    return None


def play_game():
    winner = None
    replay = 'Y'

    while replay.upper() == 'Y':
        print('Welcome to the Tic Tac Toe Game!!!')
        init()
        display_game_board()
        
        #pick marker
        marker = pick_marker()
        #set character turn
        set_player_turn(marker)

        while winner == None or len(used_numbers) < 9:
            #first turn
            print(f"{player_turn[mark_x]} (X), it's your turn")
            turn_one_num = get_number()
            #set the first play
            set_marker(turn_one_num, mark_x)
            #add number to the used_numbers
            used_numbers.append(turn_one_num)
            #display board
            display_game_board()

            #check winner
            winner = check_winner(mark_x)
            if winner != None:
                print(f'{winner} has won the game')
                break

            if len(used_numbers) == 9:
                break

            #second turn
            print(f"{player_turn[mark_o]} (O), it's your turn")
            turn_two_num = get_number()
            #set the second play
            set_marker(turn_two_num, mark_o)
            #add number to the used_numbers
            used_numbers.append(turn_two_num)
            #display board
            display_game_board()

            winner = check_winner(mark_o)
            if winner != None:
                print(f'{winner} has won the game')
                break
        
        if winner == None and len(used_numbers) == 9:
            print(f'This game is tied')

        #ask for replay
        replay = input('Would you like to replay? Y or N: ')

        while replay.upper() not in ['Y', 'N']:
            replay = input('Would you like to replay? Y or N: ')

    print('Thank you for playing Tic Tac Toe')


play_game()