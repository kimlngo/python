from collections import Counter

char_lst = ['a', 'b', 'a']
char_dict = dict(Counter(char_lst))
print(char_dict)

#iterating over items + tuple unpacking
for k,v in char_dict.items():
    print(f'key: {k}, val: {v}')

print(char_dict.items())