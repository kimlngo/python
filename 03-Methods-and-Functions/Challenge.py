print('========================================')
print('Challenging Problem')
print("SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order")

def find_first_index(num_list, number):
    '''Return the first index of number in num_list, 
        if there's no index, return None'''
    
    index = -1
    for idx, num in enumerate(num_list):
        if num == number:
            index = idx
            break

    if index != -1:
        return index
    else:
        return None
    

def is_007_exist_in_order(num_list=[]):
    if num_list.count(0) < 2 or num_list.count(7) < 1:
        return False
    
    first_zero_idx = find_first_index(num_list, 0)
    second_zero_idx = find_first_index(num_list[first_zero_idx + 1:], 0) + first_zero_idx + 1
    seven_zero_idx = find_first_index(num_list, 7)

    return first_zero_idx < second_zero_idx and second_zero_idx < seven_zero_idx

print(f'([1,2,4,0,0,7,5]) : {is_007_exist_in_order([1,2,4,0,0,7,5])}')
print(f'([1,0,2,4,0,5,7]) : {is_007_exist_in_order([1,0,2,4,0,5,7])}')
print(f'([1,7,2,0,4,5,0]) : {is_007_exist_in_order([1,7,2,0,4,5,0])}')

print('========================================')
print("COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number")
#count_primes(100) --> 25

def is_prime(num):
    sqrt = int(num ** 0.5)

    for div in range(2, sqrt + 1):
        if num % div == 0:
            return False
        
    return True

def count_primes(num):
    #check for 0 and 1
    if num < 2:
        return 0
    
    return len([n for n in range(2, num + 1) if is_prime(n)])

print(f'count_primes(100): {count_primes(100)}')