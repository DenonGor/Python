my_list = [28, 15, 36, 1, 18, 300, 97, 16]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)
