def sum_el():
    summa = 0
    while True:
        my_list = input("Введите через пробел числа для суммирования, для выхода введите q ").split()
        for i in my_list:
            if i.lower() == "q":
                return summa
            else:
                try:
                    summa += int(i)
                except ValueError:
                    print("ВВодите числа, а если хотите выйти введите q ")
        print(f"Сумма чисел равна {summa}")


print(sum_el())
