month_list = [[12, 1, 2, "Зима"], [3, 4, 5, "Весна"], [6, 7, 8, "Лето"], [9, 10, 11, "Осень"]]

month_dict = {
    (12, 1, 2): "Зима",
    (3, 4, 5): "Весна",
    (6, 7, 8): "Лето",
    (9, 10, 11): "Осень"
}

month = float(input("Введите номер месяца: "))
month = int(month // 1)

""" Решение через dict """

if 0 < month <= 12:
    for i in month_dict.keys():
        if month in i:
            print(f"Время года - {month_dict.get(i)}")
else:
    print("Такого месяца не существует!")

""" Решение через list """

if 0 < month <= 12:
    for i in month_list:
        if month in i:
            print(f"Время года - {i[-1]}")
else:
    print("Такого месяца не существует!")
