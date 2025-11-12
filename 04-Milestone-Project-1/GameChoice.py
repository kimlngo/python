def display_game(display_lst):
    print('Here is the current list: ')
    print(display_lst)

def position_choice():
    #variables
    #initial
    choice = ''
    acceptable_range = range(0,3)
    within_range = False

    while not (choice.isdigit() and within_range):
        choice = input('Please enter your choice (0, 1, 2): ')

        if not choice.isdigit():
            print('Sorry, this is not a digit')
        else:
            choice_int = int(choice)
            if choice_int in acceptable_range:
                within_range = True
            else:
                print('Sorry, this is not within range (0, 1, 2)')

    return int(choice)

def get_replacement():
    return input('Type a string to place at the position: ')

def prompt_continue_game():
    choice = ''

    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Would you like to keep playing? Y or N: ')

        if choice not in ['Y', 'N']:
            print('Sorry, please choose only Y or N')


    return choice in ['Y', 'y']

def run_game():

    #variable
    to_continue = True
    game_list = [0,1,2]
    
    while to_continue:
        #display game list
        display_game(game_list)
        
        #get user input
        index = position_choice()

        #get new value af the index
        replacement = get_replacement()

        #replace the element at the index
        game_list[index] = replacement

        #display the game list
        display_game(game_list)

        #prompt
        to_continue = prompt_continue_game()


run_game()