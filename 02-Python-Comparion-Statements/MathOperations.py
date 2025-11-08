from random import shuffle, randint

print('min, max functions')
num_list = [10,20,90,60,100,30,50]
print(f"min value: {min(num_list)}")
print(f"max value: {max(num_list)}")

print('=======================')
print('shuffle function')
print(f'before shuffle: {num_list}')
shuffle(num_list) #shuffle also works in-place like sort and reverse so not returning anything
print(f'after shuffle: {num_list}')

print('=======================')
print('random int function')
random_int = randint(0, 100)
print(f"random int: {random_int}")
print(f"random int: {randint(0,100)}")

print('=======================')
print('input function')
number_str = input('Please enter a number: ')
print(f'number: {number_str}, type: {type(number_str)}')

print('=======================')
print('casting a number')
number = int(number_str)
number_float = float(number_str)
print(f"number: {number}, type: {type(number)}")
print(f"number_float: {number_float}, type: {type(number_float)}")