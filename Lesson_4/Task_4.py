my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 56, 13, 13]
my_d = {}
for el in my_list:
    my_d[el] = my_d.get(el, 0) + 1
new_list = list({el: i for el, i in my_d.items() if i == 1})
print(new_list)
