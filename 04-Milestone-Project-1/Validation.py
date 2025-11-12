def user_choice():
    '''Return a user's choice as int and within 0-10'''

    #initial
    choice = ''
    acceptable_range = range(0, 10)
    within_range = False

    while not (choice.isdigit() and within_range):
        choice = input('Please enter a number (0 - 10): ')

        if not choice.isdigit():
            print('Sorry, this is not a digit')
        else:
            choice_int = int(choice)
            if not choice_int in acceptable_range:
                print('Sorry, this is not within acceptable range')
            else:
                within_range = True

    return int(choice)

print(f'You have entered: {user_choice()}')