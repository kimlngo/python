
x = 1024
print(f'hex of {x} is {hex(x)}')
print(f'binary of {x} is {bin(x)}')

y = 5.23222
z = round(y, 2)
print(z)

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower()) #False (Mary)

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(f'w appeared {s.count('w')} times')

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(f'element in set1 but not in set2 is {set1.difference(set2)}')
print(f'all elements that are in either set: {set1.union(set2)}')

my_dict = {x:x ** 3 for x in range(5)}
print(my_dict)

list1 = [1,2,3,4]
list1.reverse()
print(list1)

list2 = [3,4,2,5,1]
list2.sort()
print(list2)

list3 = list2[::-1]
print(list3) #reverse list