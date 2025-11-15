
#Basic try-except-else example
try:
    result = 10 + "10"
except:
    print('Something went wrong')
else:
    print('Adding went well')
    print(f'result = {result}')

print('============================')
#Finally example
try:
    f = open('test.txt', 'w')
    # f = open('test.txt', 'r')
    f.write('This is a test line')
except TypeError:
    print('There was a TypeError')
except OSError:
    print("There's an OS error")
except:
    print("All other exceptions")
finally:
    print('Always execute')

#try-except in a function
def ask_for_int():

    while True:
        try:
            number = int(input('Please enter a number: '))
        except:
            print("That's not a number, please try again")
            continue
        else:
            break
            # return number

    return number
    
print(ask_for_int())