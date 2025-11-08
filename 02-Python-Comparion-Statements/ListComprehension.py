sentence = 'Hello World'

print('create a list of chars in traditional way')
char_list = []
for c in sentence:
    char_list.append(c)
print(f"character list: {char_list}")

print('================================')
print('use list comprehension')

char_list_2 = [c for c in sentence]
print(f'char_list_2 using comprehension: {char_list_2}')

print('================================')
print('use list comprehension with range() function')

num_list = [n for n in range(0, 11)]
print(f"num_list: {num_list}")

print('================================')
print('transform the number with a mapping function')
square_num_list = [n**2 for n in range(0, 11)]
print(f"square_num_list: {square_num_list}")

print('================================')
print('transform the number with a mapping function and a filtering using if')
square_even_num_list = [n**2 for n in range(0, 11) if n % 2 == 0]
print(f"square_even_num_list: {square_even_num_list}")

print('================================')
print('nested for loops with comprehension')

result = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        result.append(x * y)

print(f"result: {result}")

result_2 = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(f"result_2: {result_2}")