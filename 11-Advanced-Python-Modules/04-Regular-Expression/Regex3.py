import re

#or operator for search
text = 'The cat is here'
print(re.search(r'cat|dog', text)) #<re.Match object; span=(4, 7), match='cat'>
text = 'The dog is here'
print(re.search(r'cat|dog', text)) #<re.Match object; span=(4, 7), match='dog'>

#wildcard operator (.)
text = "The cat in the hat went sat"
print(re.findall(r'.at', text)) #['cat', 'hat', 'sat']
print(re.findall(r'(.)at', text)) #['c', 'h', 's'] extract out the previous character
#more characters in wild cat
text = "The cat in the hat went splat"
print(re.findall(r'...at', text)) #['e cat', 'e hat', 'splat']

#startwith (^) and endwith ($)
#note that this apply the the whole sentence, not the number within the sentence
text = "1 is a good number. Good number is 2"
print(re.findall(r'^\d', text)) #['1']
print(re.findall(r'\d$', text)) #['2']
text = "I am 37 years old"
print(re.findall(r'^\d', text)) #[] doesn't find any number within
print(re.findall(r'\d$', text)) #[] doesn't find any number within

#exclusion
text = "there are 3 numbers 34 inside 5 this sentence"
print(re.findall(r'[^\d]+', text)) #exclude numbers within a sentence. The + sign is used to combine the chars together
#['there are ', ' numbers ', ' inside ', ' this sentence']

#use exclusion to exlude the punctuation and spaces
text = "This is a string! But it has punctuation. How can we remove it?"
rmv_punc = r'[^!.? ]+'
words = re.findall(rmv_punc, text)
print(words) #['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']

# we can then join the words to form a sentence
print(" ".join(words)) #This is a string But it has punctuation How can we remove it

#inclusion
text = "Only find the hyphen-words in the sentence. But we do not know how long-ish they are"
inc_hyphen = r'[\w]+-[\w]+'
print(re.findall(inc_hyphen, text)) #['hyphen-words', 'long-ish']

#search for multiple matches
text = 'one catfish;'
text2 = 'two catnap?'
text3 = 'three caterpilla!'

search_ptrn = r'cat(fish|nap|yelly)'
print(re.search(search_ptrn, text)) #<re.Match object; span=(4, 11), match='catfish'>
print(re.search(search_ptrn, text2)) #<re.Match object; span=(4, 10), match='catnap'>
print(re.search(search_ptrn, text3)) #None
