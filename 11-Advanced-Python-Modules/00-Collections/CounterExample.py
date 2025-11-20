from collections import Counter

#Counter
#Build frequency map
lst = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,5,5,5,6,6,6,6]
freq_counter = Counter(lst)
print(freq_counter) #Counter({3: 5, 5: 5, 1: 4, 2: 4, 6: 4, 4: 3})
print(freq_counter[1]) #4
print(freq_counter[3]) #5

#Counter with string
str = 'aaaaaabbbbbbcccccccccddddddddddeeeeeeeffffffff'
str_counter = Counter(str)
print(str_counter) #Counter({'d': 10, 'c': 9, 'f': 8, 'e': 7, 'a': 6, 'b': 6})
print(str_counter['a']) #6

#Counter with words in a sentence
sentence = "How many times does each word show up in this sentence word times each each word"

word_counter = Counter(sentence.split())
print(word_counter) #Counter({'each': 3, 'word': 3, 'times': 2, 'How': 1, 'many': 1, 'does': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentence': 1})
print(word_counter['word']) #3

#more functions:
print(sum(str_counter.values())) #46
str_map = dict(str_counter)
print(str_map)