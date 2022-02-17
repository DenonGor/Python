with open("text_4.txt", "r", encoding="utf-8") as my_text:
    my_line = my_text.readlines()
    for i, word in enumerate(my_line, 1):
        words = len(word.split())
        print(f"Строка {i} содержит {words} слов")
