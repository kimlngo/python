from performance import benchmark_execution

def func_one():
    return 1

print(f'fun_one call: {func_one()}')

fn_one_copy = func_one
print(f'fn_one_copy call: {fn_one_copy()}')

print('--delete func_one---')
del func_one
print(f'fn_one_copy re-call: {fn_one_copy()}')

def is_even(num):
    return num % 2 == 0

num_list = list(range(100))
print(f'num_list: {num_list}')

even_number = list(filter(is_even, num_list))
print(f'even_number: {even_number}')

print('=====================')
def hello(name='Kim'):
    print('Executing function hello')

    def greet():
        return '\tThis is greet() func inside hello'
    
    def welcome():
        return '\tThis is welcome() func inside hellow'
    
    if name == 'Kim':
        return greet
    else:
        return welcome
    
print(hello('Kim')) #<function hello.<locals>.greet at 0x000001EC52258180>
print(hello('An'))  #<function hello.<locals>.welcome at 0x000001F82CB28360>

print(hello('Kim')())
#Executing function hello
    #This is greet() func inside hello

print(hello('An')())
#Executing function hello
    #This is welcome() func inside hello

print('=========== decorator ===========')

def decorate_fn(orig_fn):
    def wrap_fn():
        print('Decoration BEFORE orig_fn')

        orig_fn()

        print('Decoration AFTER orig_fn')

    return wrap_fn

def say_hello():
    print("Hello World! I'm Thomas")

hello_decorated = decorate_fn(say_hello)
hello_decorated()
#Decoration BEFORE orig_fn
#Hello World! I'm Thomas
#Decoration AFTER orig_fn

#using decorator annotation @
print('============= using annotation =============')
@decorate_fn
@benchmark_execution
def greet_world():
    print("Hello World, I'm a better version of myself each day")

greet_world()
##Decoration BEFORE orig_fn
#Hello World, I'm a better version of myself each day
#Execution takes: 0.0001842975616455078
#Decoration AFTER orig_fn