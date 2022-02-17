import json

with open("text_77.json", "w", encoding="utf-8") as w_file:
    with open("text_7.txt", encoding="utf-8") as r_file:
        a_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in r_file}
        res = [a_dict, {"average_profit": round(sum([int(i) for i in a_dict.values() if int(i) > 0]) /
                                                len([int(i) for i in a_dict.values() if int(i) > 0]))}]
    json.dump(res, w_file, ensure_ascii=False, indent=4)
