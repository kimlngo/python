import math
import random

#Rounding numbers
value = 3.45
print(math.floor(value))
print(math.ceil(value))

print(round(3.5)) #4
print(round(4.5)) #4

#math constant
print(math.pi)
print(math.e)

#randint
rand_int = random.randint(0,100)
print(rand_int)

#setting the seed will make the randint produce predefined number in a sequence
# random.seed(101)

# for n in range(0,5):
#     print(f'({n + 1}): {random.randint(0,100)}') #74-24-69-45-59

#randomly select a number or numbers from a list
nums = list(range(1,44)) #1 - 43

print(f'Select one random num from list: {random.choice(nums)}')
print(f'Select multiple numbers from a list with duplication: {random.choices(population=nums,k=10)}')
print(f'Select multiple numbers from a list WITHOUT duplication: {random.sample(population=nums,k=10)}')