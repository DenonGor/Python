def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Не выполнено условие ввода данных: " \
                   "x - должен быть положительным " \
                   "y - должен быть отрицательным"
        else:
            res = x ** y
            return round(res, 10)
    except ValueError:
        return 'Вводите только числа'


print(my_func(input("введите действительное положительное x: "), input("введите отрицательный и целый y: ")))
