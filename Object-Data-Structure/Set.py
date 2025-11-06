#set
my_set = set()

# add element
my_set.add(1)
my_set.add(2)
print(my_set) #{1, 2}

my_set.add(2)
print(my_set) #{1, 2}

#casting a list to set to remove duplicates
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
unique_nums = set(my_list)
print(f'unique_nums: {unique_nums}')