import math, string

def calculate_sphere_volume(radius):
    return 4 * math.pi * (radius ** 3) / 3

print('===========================')
print('Q1. Calculate sphere volume')
print(f'volume = {calculate_sphere_volume(2)}')

print('===========================')
print('Q2. Check number in given range')

def ran_check_bool(num, low, high):
    return low <= num and num <= high

def ran_check_print(num, low, high):
    if ran_check_bool(num, low, high):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is NOT in the range between {low} and {high}')

print(f'ran_check(5,2,7)? {ran_check_bool(5,2,7)}')
ran_check_print(5,2,7)

print('===========================')
print('Q3. Calculate the number of uppercase & lowercase letter')

def up_low_iterative(str):
    up_count = 0
    low_count = 0

    for letter in str:
        if letter.lower() in string.ascii_lowercase:
            if letter.isupper():
                up_count += 1
            else:
                low_count += 1

    print(f'No. of Upper case characters : {up_count}')
    print(f'No. of Lower case characters : {low_count}')

up_low_iterative('Hello Mr. Rogers, how are you this fine Tuesday?')

def up_low_declarative(str):
    upper_letters = list(filter(lambda l:l.lower() in string.ascii_letters and l.isupper(), str))
    lower_letters = list(filter(lambda l:l.lower() in string.ascii_letters and l.islower(), str))

    print(f'Declarative - No. of Upper case characters : {len(upper_letters)}')
    print(f'Declarative - No. of Lower case characters : {len(lower_letters)}')

up_low_declarative('Hello Mr. Rogers, how are you this fine Tuesday?')


print('===========================')
print('Q4. Return unique numbers')

def unique_list(num_list):
    return list(set(num_list))

print(f'unique numbers: {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}')


print('===========================')
print('Q5. Multiply all numbers in a list')

def multiply_all_nums(numbers):
    product = 1
    for num in numbers:
        product *= num
    
    return product

print(f'product of multiplying numbers: {multiply_all_nums([1, 2, 3, -4])}')

print('===========================')
print('Q6. Is Palindrome')
def is_palindrome(str):
    no_space_str = str.replace(' ', '')
    reverse_str = no_space_str[::-1]

    return no_space_str == reverse_str

print(f'madam? - {is_palindrome('madam')}')
print(f'nurses run? - {is_palindrome('nurses run')}')
print(f'kayak? - {is_palindrome('kayak')}')
print(f'hello? - {is_palindrome('hello')}')


print('===========================')
print('Q7. Pangram')

def is_pangram(str, alphabet = string.ascii_lowercase):
    str_no_space = str.replace(' ', '').lower()
    unique_chars = list(set(str_no_space))

    return len(unique_chars) == len(alphabet)

def create_freq_counter(str):
    freq_map = {}
    
    for letter in str:
        if freq_map.get(letter) == None:
            freq_map[letter] = 0
        
        freq_map[letter] += 1

    return freq_map

def is_pangram_2(str, alphabet = string.ascii_lowercase):
    normalized_str = str.replace(' ', '').lower()
    freq_map = create_freq_counter(normalized_str)
    print(f'freq_map: {freq_map}')

    for char in alphabet:
        if freq_map.get(char) == None or freq_map.get(char) < 1:
            print(f'Missing char: {char}')
            return False

    return True

print(f'test pangram: {is_pangram("The quick brown fox jumps over the lazy dog")}')
print(f'test pangram: {is_pangram("I am living in Jacksonville")}')

print(f'test pangram 2: {is_pangram_2("The quick brown fox jumps over the lazy dog")}')
print(f'test pangram 2: {is_pangram_2("I am living in Jacksonville")}')