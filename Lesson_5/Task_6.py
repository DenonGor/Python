my_dict = {}
with open("text_6.txt", encoding="utf-8") as f:
    for line in f:
        name, nums = line.split(":")
        name_s = sum(map(int, "".join([i for i in nums if i == " " or "0" <= i <= "9"]).split()))
        my_dict[name] = name_s
print(f"{my_dict}")
