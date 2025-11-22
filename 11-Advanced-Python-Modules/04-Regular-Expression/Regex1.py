import re

text = "The agent's phone number is 910-555-6666. Call soon!"
print('phone' in text) #True

#using re to search
pattern = 'phone'
match = re.search(pattern, text)
print(match) #<re.Match object; span=(12, 17), match='phone'>
print(match.span()) #(12, 17)
print(match.start()) #12
print(match.end())   #17

print(re.search('not found', text)) #None

#search only find the first appearance, to find all the appearance, use findall and finditer
text = "My phone number is 910-555-6666 and it is a nice phone number"
matches = re.findall(pattern, text)
print(matches) #['phone', 'phone']
print(len(matches)) #2

for txt_match in re.finditer(pattern, text):
    print(txt_match)
#<re.Match object; span=(3, 8), match='phone'>
#<re.Match object; span=(49, 54), match='phone'>