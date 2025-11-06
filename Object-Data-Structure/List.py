#list
my_list = [1,2,3]

#len of list
print(len(my_list))

#accessing list element
print(f'first element of my_list: {my_list[0]}') #1

#concatenate two lists
your_list = [4, 5, 6]
new_list = my_list + your_list
print(f'Concatenated list: {new_list}') #[1, 2, 3, 4, 5, 6]

#slicing in list is like string
sub_list = new_list[2:]
print(f'sub_list: {sub_list}')
print(f'sub list with jump: {new_list[::2]}') #1, 3, 5

#list is mutable
new_list[0] = 1.5
print(f'new_list: {new_list}')

#append method
new_list.append(7)
print(f'new_list: {new_list}')

#pop/remove element of a list
last_element = new_list.pop()
print(f'last_element: {last_element}')
print(f'new_list: {new_list}')

#remove an element at a specific index of the list
pop_element = new_list.pop(0) #1.5
print(f'pop_element: {pop_element}')
print(f'new_list: {new_list}')

#out of range error
#print(new_list.pop(5))

#sorting a list
alphabet_list = ['a', 'x', 'b', 'k', 'z', 'f']
alphabet_list.sort()
print(f'sorted alphabet list: {alphabet_list}')

#note that sort() method sort in-place and return nothing (None) so 
#do not reassign the sort() method call to a variable like in Java
#sorted_alpha_list = alphabet_list.sort() ==> sorted_alpha_list = None
num_list = [5, 3, 1, 7, 2, 4, 9]
num_list.sort()
print(f'sorted num_list: {num_list}')

#reverse a list
num_list.reverse()
print(f'Reverse num_list: {num_list}')
