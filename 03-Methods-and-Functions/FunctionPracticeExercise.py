print('Warm Up Section')

print('Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd')

def is_even(num):
    return num % 2 == 0

def lesser_of_two_evens(a,b):
    if is_even(a) and is_even(b):
        return min(a,b)
    else:
        return max(a,b)
    
print(lesser_of_two_evens(2,4)) #2
print(lesser_of_two_evens(2,5)) #5

print('========================================')
print('ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter')

def animal_crackers(str):
    words = str.split()
    return words[0][0] == words[1][0]

print(animal_crackers('Levelheaded Llama')) #True
print(animal_crackers('Crazy Kangaroo')) #False

print('========================================')
print('MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False')

def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20,10)) # True
print(makes_twenty(12,8)) # True
print(makes_twenty(2,3)) # False
