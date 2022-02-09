def my_func(el_1, el_2, el_3):
    try:
        return sum(sorted([int(el_1), int(el_2), int(el_3)])[1:])
    except ValueError:
        return "Вводите только числа"


print(my_func(input("Введите первый аргумент"), input("Введите второй аргумент"), input("Введите третий аргумент")))
