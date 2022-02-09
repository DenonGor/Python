def my_del(arg_1, arg_2):
    try:
        return round((arg_1 / arg_2), 3)
    except ZeroDivisionError:
        return "Деление на ноль не возможно!"


print(my_del(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
