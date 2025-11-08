#ref: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/07-Statements%20Assessment%20Test.ipynb

print("Question 1: Use for, .split(), and if to create a Statement that will print out words that start with 's':")
st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if(word[0] == 's'):
        print(word)

print('===============================')
print("Question 2: Use range() to print all the even numbers from 0 to 10.")

for num in range(0, 11, 2):
    print(num)

print('===============================')
print("Question 3: Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.")
divide_by_three = [num for num in range(1, 51) if num % 3 == 0]
print(f"list of all numbers between 1 and 50 that are divisible by 3. \n{divide_by_three}")

print('===============================')
print("Question 4: Go through the string below and if the length of a word is even print 'even!'")
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(f'{word} - even!')

print('===============================')
print('Question 5: Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".')

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} - FizzBuzz')
    elif num % 3 == 0:
        print(f'{num} - Fizz')
    elif num % 5 == 0:
        print(f'{num} - Buzz')
    else:
        print(num)

print('===============================')
print("Question 6: Use List Comprehension to create a list of the first letters of every word in the string below:")
st = 'Create a list of the first letters of every word in this string'

first_letters = [word[0] for word in st.split()]
print(f"first letter list: {first_letters}")