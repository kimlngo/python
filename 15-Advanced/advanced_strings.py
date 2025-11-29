s = 'hello world'

#changing case
print(s.capitalize()) #Hello world
print(s.upper())      #HELLO WORLD
print(s.lower())      #hello world
print(s.title())      #Hello World (cap each first letter of each word)

#count character appearance
print(s.count('o'))  #2
print(s.count('l'))  #3

#find first appearance of a character
print(s.find('l')) #2
print(s.find('a')) #-1

#check if a string is alphanumeric
s = 'hello'
print(s.isalnum()) #True
print(s.isalpha()) #True
print(s.isnumeric()) #False

#checking the case
print(s.islower()) #True
print(s.isupper()) #False
print(s.isspace()) #False
print('     \t     '.isspace()) #True
print('Hello A World!'.istitle()) #True
print('Hello a World!'.istitle()) #False

#startswith and endswith
print(s.startswith('h')) #True
print(s.endswith('o')) #True

#Split (i.e., split at every character)
s = 'hello, there is an elephant'
print(s.split('e')) #['h', 'llo, th', 'r', ' is an ', 'l', 'phant']

#Partitition (i.e., split at only the first character and returning the front-the char-the back) as a tuple
print(s.partition('e')) #('h', 'e', 'llo, there is an elephant')