my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(f'hello {num}')

print('\nPrint even numbers only:')

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

sum = 0
for num in my_list:
    sum += num

print(f'Total sum is: {sum}')

print('\nPrint each character')
message = 'The quick brown fox'

for letter in message:
    print(letter)

print('\nPrint tuple')
tup = (1,2,3)

for t in tup:
    print(t)

print('\nTuple with List and unpacking')
tuple_list = [(1,2), (3,4), (5,6), (7,8)]

for first, second in tuple_list:
    print(f'first: {first}, second: {second}')

print('\nIterate through Dictionary')
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}

for item in my_dict:
    print(item) #only the key is printed out

for tup in my_dict.items():
    print(tup) #print out each tuple pair

for key, val in my_dict.items():
    print(f'key: {key}, value: {val}') #accessing key-value explicitly


print('\nwhile loop exercise')
x = 10

while x < 5:
    print(f'x = {x}')
    x += 1
else:
    print('x is not less than 5 any more')

print('\nbreak, continue, pass')