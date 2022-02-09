second = int(input("введите количество секунд: "))
hour = second // 3600
minute = ((second % 3600) // 60)
seconds = (((second % 3600) % 60))
print(f"{hour:02}:{minute:02}:{seconds:02}")
