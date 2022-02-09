rev = int(input("Введите выручку предприятия: "))
cost = int(input("Введите издержки предприятия: "))
result = rev - cost
if result < 0:
    print("Убыток - выручка меньше издержек")
elif result == 0:
    print("Фирма сработала в ноль - выручка равна издержкам")
else:
    print("Прибыль - выручка больше издержек")
    rent = result / rev
    print(f"Рентабельность фирмы: {rent:.2f}")
    workers = int(input("Введите количество работников"))
    w_result = result / workers
    print(f"Прибыль фирмы в расчете на одного сотрудника: {w_result:.2f}")
