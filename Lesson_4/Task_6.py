from itertools import count
from itertools import cycle

a = count(3)
b = cycle("ABCD")

for _ in range(8):
    print(next(a), next(b))
