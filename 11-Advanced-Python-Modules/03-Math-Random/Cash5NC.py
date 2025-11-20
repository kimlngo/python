import random

pools = list(range(1,44))

print('Random pick')
random_picked = random.sample(population=pools, k=5)
random_picked.sort()
print(random_picked)