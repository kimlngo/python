x = 25

def printer():
    x = 50
    return x

print(x) #25
print(printer()) #50

#LEGB Rule: Local, Enclosing, Global, Built-in
#LOCAL:
lambda num : num ** 2

#ENCLOSING:
#GLOBAL
name = 'GLOBAL'

def greet():
    #ENCLOSING
    name = 'John'

    def hello():
        #LOCAL
        name = 'Matthew'
        print('Hello ' + name)

    hello()

greet() #Hello Matthew

#printer_2() affect global variable
def printer_2():
    global x #should be avoided
    print(f'x before (global): {x}')

    x = 'new value'
    print(f'x after (global): {x}')

print(f'x global printer_2(): {x}') #25
printer_2()
print(f'x global printer_2(): {x}') #new value

print('==================================')
x = 25
#printer_3() return the new value
def printer_3():
    x = 'new car'
    print(f'x after: {x}')

    return x

print(f'x global printer_3(): {x}') #25
x = printer_3()
print(f'x global printer_3(): {x}') #new car
