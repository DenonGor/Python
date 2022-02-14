from sys import argv

name, tim_w, sta_w, prem_w = argv
print(argv)
print(f"Время работы сотрудника: {tim_w} часов")
print(f"Ставка в час           : {sta_w} руб.")
print(f"Премия сотрудника      : {prem_w} руб.")
x, y, z = int(tim_w), int(sta_w), int(prem_w)


def zp_w():
    return (x * y) + z


print(f"Сотрудник заработал    : {zp_w()} руб.")
