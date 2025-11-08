# age = int(input('How old are you? '))
age = 25

#logical operator and, or, not
if age >= 20 and age < 30:
    print('You are young!')
elif age < 20:
    print('You are still teenager')
else:
    print('Age does not matter')


if age == 25 or age == 30:
    print('Oh! You are either 25 or 30 years old')


name = 'Thomas'
if not name == 'John':
    print('You are not John')
else:
    print('Hello John')
