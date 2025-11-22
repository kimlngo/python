import re

#Character Identifier
text = "My phone number is 910-555-6666"
phone_search = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone_search) #<re.Match object; span=(19, 31), match='910-555-6666'>
print(phone_search.span()) #(19, 31
print(phone_search.group()) #910-555-6666

#Quantifiers
phone_search_quantifier = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone_search_quantifier) ##<re.Match object; span=(19, 31), match='910-555-6666'>

#Using quantifier and grouping
print('======== Using quantifier and grouping ========')
compile_ptn = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
area_code_search = re.search(compile_ptn, text) 
print(area_code_search) #<re.Match object; span=(19, 31), match='910-555-6666'>
print(type(area_code_search))
print(area_code_search.group()) #910-555-6666
print(area_code_search.group(1)) #910. note that this is not zero-based
print(area_code_search.group(2)) #555
print(area_code_search.group(3)) #6666