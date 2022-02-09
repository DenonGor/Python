def int_func(word):
    latin_ch = 'qwertyuiopasdfghjklzxcvbnm'
    return word.capitalize() if set(word) <= set(latin_ch) else False


words = input("введите слова маленькими латинскими буквами через пробел").split()
for i in words:
    res = int_func(i)
    if res:
        print(int_func(i), end=" ")
