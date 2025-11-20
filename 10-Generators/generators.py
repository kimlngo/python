
def create_cubes(n):
    for i in range(n):
        yield i ** 3

for i in create_cubes(10):
    print(i)

all_cubes = list(create_cubes(10))
print(f'all cubes: {all_cubes}')