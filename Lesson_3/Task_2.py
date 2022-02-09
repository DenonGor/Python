def pers_data(name, surname, birthday, city, email, phone):
    return f'Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city}; Email - {email}; Phone - {phone}'


print(pers_data(name=input("введите свое имя: "), surname=input("введите свою фамилию: "),
                birthday=input("введите свой день рождения dd.mm.yy: "),
                city=input("введите свой город проживания: "), email=input("введите свой email: "),
                phone=input("введите свой телефон: ")))
