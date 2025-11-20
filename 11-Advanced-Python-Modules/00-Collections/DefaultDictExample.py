from collections import defaultdict

dft_dict = defaultdict(lambda: 0)
str = 'aaaabbbbcccdddd'

for letter in str:
    dft_dict[letter] += 1

print(f'freq counter map: {dft_dict}')