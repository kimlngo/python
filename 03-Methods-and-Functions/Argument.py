print('========================')
print('*args exercise') #*args is like variable arguments
def five_percent_of_all(*args):
    print(args) #(1, 2, 3, 4, 5)
    print(type(args)) #<class 'tuple'>
    return sum(args) * 0.05

print(five_percent_of_all(1,2,3,4,5)) #0.75

print('========================')
print('**kwargs exercise')

def find_fruit(**kwargs):
    print(kwargs) #{'fruit': 'apple', 'weight': 200} | {'dessert': 'apple', 'weight': 200}
    if 'fruit' in kwargs:
        print(f"The fruit is {kwargs['fruit']}")
    else:
        print('No fruit is found')

find_fruit(fruit='apple', weight=200) #The fruit is apple
find_fruit(dessert='apple', weight=200) #No fruit is found

print('========================')
print('*args & **kwargs combine exercise')

def order(*args, **kwargs):
    print(args)
    print(kwargs)

    print(f"I'd like to order {args[0]} {kwargs['fruit']}")

order(10,20,30,food='cheese',fruit='apple',stationary='paper')
