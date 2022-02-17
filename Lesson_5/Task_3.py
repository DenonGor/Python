with open("text_3.txt", "r", encoding="utf-8") as my_text:
    emp_dic = {line.split()[0]: float(line.split()[1]) for line in my_text}
    print(f"Список сотрудников с окладом менее 20 тыр {[i[0] for i in emp_dic.items() if i[1] < 20000]}\n"
          f"Средняя величина дохода всех сотрудников: {round(sum(emp_dic.values()) / len(emp_dic), 2)}")
