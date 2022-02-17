print("Введите данные строки. Для завершения введите пустую строку")
with open("text_task_1.txt", "w", encoding="UTF-8") as my_text:
    line = " "
    while line != "":
        line = input()
        print(line, file=my_text)
