# number = input("Введите число: ")
# m = int(len(number)) - 1
# n = 0
# maxim = int(number[0])
# while m >= n:
#    if maxim < int(number[n]):
#        maxim = int(number[n])
#        n += 1
#    else:
#        n += 1
# print(maxim)
number = int(input("Введите число: "))
n = number % 10
num = number // 10
while num != 0:
    if n < num % 10:
        n = num % 10
        num = num // 10
    else:
        num = num // 10
print(n)