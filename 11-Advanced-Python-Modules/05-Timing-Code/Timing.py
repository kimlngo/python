import timeit

def num_to_string_one(n):
    return [str(num) for num in range(n)]

def num_to_string_two(n):
    return list(map(str,range(n)))

stmt1 = '''
num_to_string_one(10000) 
'''
setup1 = '''
def num_to_string_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt1, setup1, number=10000))

stmt2 = '''
num_to_string_two(10000)
'''
setup2 = '''
def num_to_string_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2, setup2, number=10000))