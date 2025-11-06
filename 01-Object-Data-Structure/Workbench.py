message = 'hello'

print(message[0]) #h
print(message[-1]) #o
print(len(message)) #5

#slicing
alphabet = 'abcdefgh'
           #0123456
print(alphabet[2:]) # from index 2 to the end ==> cdefgh
print(alphabet[:3]) # from begining to index 3 but not including ==> abc
print(alphabet[2:4]) # from index 2 to index 4 (not included) ==> cd

print(alphabet[::2]) # from begining to the end with stepping of 2 ==> aceg
print(alphabet[::-1]) # easy reversing a string ==> hgfedcba

#multiplication of letters in String
print(10 * 'a') #aaaaaaaaaa

x = 'Hello World'
print(x.upper())
print(x.split()) #['Hello', 'World']

#print format
print('Hello, my first name is {} and my last name is {}.'.format('Kim Long', 'Ngo'))

#print format with index position
print('The {} {} {}'.format('fox', 'brown', 'quick')) #The fox brown quick
print('The {2} {1} {0}'.format('fox', 'brown', 'quick')) #The quick brown fox (using the index)
print('The {0} {0} {0}'.format('fox', 'brown', 'quick')) #The fox fox fox

#format with named variable
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) #The quick brown fox || easier and more intuitive than using index

print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick')) #The fox fox fox 

#float formatting {value:width.precision f}
result = 100/7
print(result)
print('Result with formatting {r:1.3f}'.format(r=result))

#f format string (String interpolation)
print(f"This is the message '{message}'")
print(f'Result printed by f string {result:1.3f}')
