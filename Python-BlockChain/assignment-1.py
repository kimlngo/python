name = input("Please enter your name: ")
age = input("Please enter your age: ")

def print_name_age():
    print("Hello " + name + ", you are " + age + " years old")


def print_anything(arg1, arg2):
    print("Argument 1 = " + arg1 + ", Argument 2 = " + arg2)


def calc_num_decades(age):
    return int(age) // 10

print_name_age()
print_anything(name, age)
print(calc_num_decades(age))
