def fact(n):
    com = 1
    for i in range(1, n + 1):
        yield f"{i}! = {com}"
        com *= (i + 1)


for el in fact(int(input("введите число для вычисления факториала: "))):
    print(el)