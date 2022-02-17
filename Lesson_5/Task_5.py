with open("text_5.txt", mode="w+", encoding="utf-8") as f:
    my_list = input("введите числа через пробел: ")
    f.write("".join(map(str, my_list)))
    f.seek(0)
    print(f"сумма чисел равна: {sum(map(int,f.readline().split()))}")
