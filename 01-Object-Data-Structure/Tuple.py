#Tuple
t = (1,2,3)
my_list = [1,2,3]
print(type(t))
print(type(my_list))

print(f'tuple t length: {len(t)}')

#accessing individual element
print(f'2nd element of tuple t: {t[1]}')

#count and index of
t = ('a', 'a', 'b')
print(f"'a' appears {t.count('a')} times")
print(f"first index of 'a' is {t.index('a')}") #0
print(f"first index of 'b' is {t.index('b')}") #2
