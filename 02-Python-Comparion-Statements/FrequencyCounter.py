name = 'abcABC'

freq_map = {}

# for character in name:
#     if char_dict.get(character) == None:
#         char_dict[character] = 0
    
#     char_dict[character] += 1

for char in name:
    if not char in freq_map:
        freq_map[char] = 0

    freq_map[char] += 1


print(f"Frequency Counter map: {freq_map}")