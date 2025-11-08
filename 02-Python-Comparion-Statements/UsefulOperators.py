#range function
print('print from 0 to 9')
for num in range(10):
    print(num)

print('=====================')
print('print from 3 to 9')
for num in range(3,10):
    print(num)

print('=====================')
print('print from 0 to 10 with step size of 2')
for num in range(0, 10, 2):
    print(num)

print('=====================')
print('generate numbers and assign to a list')
num_list = list(range(0,100,2))
print(f'num list = {num_list}')

print('=====================')
print('enumarate function')
string = 'abcdef'

for item in enumerate(string):
    print(f'{item}')
    """ (0, 'a')
        (1, 'b')
        (2, 'c')
        (3, 'd')
        (4, 'e')
        (5, 'f') """
    
#unpacking
for (index,letter)in enumerate(string):
    print(f'index: {index}, letter: {letter}')

print('=====================')
print('zip function')
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [100,200,300]

for item in zip(list1,list2,list3):
    print(item)
    """ (1, 'a', 100)
        (2, 'b', 200)
        (3, 'c', 300) """
    
#unpacking
print('unpacking with zip')
for first, second, third in zip(list1, list2, list3):
    print(f'first: {first}, second: {second}, third: {third}')
    """ first: 1, second: a, third: 100
        first: 2, second: b, third: 200
        first: 3, second: c, third: 300 """

#note: if the list in zip function has different length, zip will only zip the shortest length
list2.append('d')
zip_list = list(zip(list1, list2, list3))
print(f'zip list: {zip_list}') #'d' in list 2 is ignored

print('==========================')
print('in keyword')

print(f'is 2 in list1? {2 in list1}') #True
print(f"is char a in string def? {'a' in 'def'}") #False

#check for a key exist in dictionary
my_dict = {'k1': 'v1', 'k2': 'v2'}
print(f"is k1 in my_dict? {'k1' in my_dict}") #True
print(f"is k3 in my_dict? {'k3' in my_dict}") #False

#check for a value exist in values of dictionary
print(f"is v2 in my_dict values? {'v2' in my_dict.values()}") #True