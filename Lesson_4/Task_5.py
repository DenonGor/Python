from functools import reduce

x = reduce(lambda a, b: a * b, [i for i in range(100, 1001, 2)])
print(x)
