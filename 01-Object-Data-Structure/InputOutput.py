my_file = open('test.txt')

print(my_file.read())

# reset cursor
my_file.seek(0)
print(my_file.readlines())

my_file.close()

#new way (no close is needed)
print('new way of opening file')
with open('test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)

# write to a file
with open('myfile.txt', mode='r') as f:
    print(f.read())

# appending
with open('myfile.txt', mode='a') as f:
    f.write('\n4 - Four')


with open('yourfile.txt', mode='w') as f:
    f.write('I created this file!!!')


with open('yourfile.txt', mode='r') as f:
    print(f.read())