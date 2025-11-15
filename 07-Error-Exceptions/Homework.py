def square_number(num_list):
    try:
        return list(map(lambda n : n**2, num_list))
    except TypeError:
        print('There is a TypeError happened')
    except:
        print('Something has gone wrong')

print(f'square_number: {square_number(['a', 'b', 'c'])}')
print(f'square_number: {square_number([1,2,3])}')

print('===================================')
def divide_numbers(a, b):
    '''return the division of a over b'''
    try:
        return a / b
    except ZeroDivisionError:
        print("There is a zero division happened")
    finally:
        print('Finally All Done!')

print(f'5/3 = {divide_numbers(5,3)}')
print(f'5/3 = {divide_numbers(5,0)}')

print('===================================')

def get_square_number():
    while True:
        try:
            num = int(input("Input an integer: "))
        except:
            print('An error occurred! Please try again')
            continue
        else:
            print(f'Thank you, your number squared is: {num ** 2}')
            break

get_square_number()