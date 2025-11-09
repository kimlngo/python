print('===================================')
print('map function')
def square(num):
    return num ** 2

num_list = [1,2,3,4,5]
square_list = list(map(square, num_list))
print(f'square numbers: {square_list}') # [1, 4, 9, 16, 25]
print(f'orig num_list: {num_list}') #num_list is still unchanged [1, 2, 3, 4, 5]


print('===================================')
print('filter function')

def is_even(num):
    return num % 2 == 0

even_nums = list(filter(is_even, num_list))
print(f'even numbers: {even_nums}')  # [2, 4]
print(f'orig num_list: {num_list}')  # [1, 2, 3, 4, 5]


print('===================================')
print('lambda expression')

print('map using lambda exp')
# square_2 = lambda num : num ** 2
square_num_2 = list(map(lambda num: num ** 2, num_list))
print(f'square numbers: {square_num_2}')

print('filter using lambda exp')
even_nums_2 = list(filter(lambda num: num % 2 == 0, num_list))
print(f'even numbers: {even_nums_2}')