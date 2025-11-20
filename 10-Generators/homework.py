import random

print('##### Problem 1 #####')
def generate_squares(n):
    for num in range(n):
        yield num ** 2

for n in generate_squares(10):
    print(n)


print('##### Problem 2 #####')
def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)


print('##### Problem 2 #####')
s = 'hello'
str_iterator = iter(s)
print(next(str_iterator))


print('##### Problem Extra Credit #####')
my_list = [1,2,3,4,5]

gen_comp = (x for x in my_list if x > 3)

for n in gen_comp:
    print(n)