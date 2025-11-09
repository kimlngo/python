from random import shuffle

my_list = [1,2,3]

print('====================')
print('insert function')
#insert the value to the position before the index
my_list.insert(0, 0) #index, value
print(f'my_list: {my_list}') #[0,1,2,3]

print('====================')
print('creating function')

def say_hello():
    print('Hello')
    print('How')
    print('are')
    print('you')


def say_hello(name="World"):
    print(f"Hello {name}")

say_hello()
say_hello("Thomas")

def add_num(num1, num2):
    return num1 + num2

print(f'add_num(20,30): {add_num(20,30)}')

print('====================')
print('function with logic')

def is_even(number):
    return number % 2 == 0

print(f'is 4 even? {is_even(4)}') #True
print(f'is 7 even? {is_even(7)}') #False

def contains_even_number(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        
    return False

even_list = [1,3,5,8]
odd_list = [1,3,5,7]

print(f'contains even number {even_list}? {contains_even_number(even_list)}') #True
print(f'contains even number {odd_list}? {contains_even_number(odd_list)}') #True


print('====================')
print('Check and return all even numbers in a list')

def get_all_even_numbers(num_list):
    return [num for num in num_list if num % 2 == 0]

print(f'get all even numbers in [1,3,5,7,8,4,2,6]: {get_all_even_numbers([1,3,5,7,8,4,2,6])}')

print('====================')
print('Returing Tuple from function with unpacking')

work_hours = [('Abby', 100), ('McDonalds', 800), ('Chick-f-A', 500)]

def find_employee_of_month(work_hours):
    max_hours = 0
    emp_of_month = ''

    for emp_name, hours in work_hours:
        if hours > max_hours:
            max_hours = hours
            emp_of_month = emp_name

    return (emp_of_month, max_hours)

print(f"Employee of the month: {find_employee_of_month(work_hours)}")
print('unpacking the return tuple')

emp_name, max_hour = find_employee_of_month(work_hours)
print(f'Employee of the month: name = {emp_name}, working hours = {max_hour}')

def shuffle_and_return(input_list):
    shuffle(input_list)
    return input_list

print('====================')
print('Shuffle and Return')
my_list = [1,2,3,4,5,6,7]
print(shuffle_and_return(my_list))

print('====================')
print('Implement Guessing Game')

def get_user_guess():
    user_guest = ' '

    while user_guest not in ['0', '1', '2']:
        user_guest = input('Please enter a guess (0, 1, 2): ')

    return int(user_guest)

def check_user_guess(position_list, user_guest):
    if(position_list[user_guest] == 'O'):
        return 'Bingo'
    else:
        print(position_list)
        return 'Wrong!!!'

#create a list of 3 items
position_list = ['O', ' ', ' ']

#shuffle that list
shuffled_list = shuffle_and_return(position_list)

#ask for user's guess input
user_guest = get_user_guess()

#check if user's guess is correct
print(check_user_guess(shuffled_list, user_guest))