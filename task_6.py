product_list = []

pos_num = int(input("Введите количество позиций: "))
str_num = 1

title_list = []
price_list = []
quantity_list = []
unit_measure_list = []

while pos_num > 0:
    title = input(f"Введите название товара №{str_num}: ")
    price = int(input(f"Введите цену товара №{str_num}: "))
    quantity = int(input(f"Введите количество товара №{str_num}: "))
    unit_measure = input(f"Введите единицу измерения товара №{str_num}: ")

    title_list.append(title)
    price_list.append(price)
    quantity_list.append(quantity)
    if unit_measure not in unit_measure_list:
        unit_measure_list.append(unit_measure)

    temp_dict = {
        "название": title,
        "цена": price,
        "количество": quantity,
        "ед": unit_measure
    }

    product_list.append((str_num, temp_dict))
    pos_num -= 1
    str_num += 1

prod_dict = {
    "название": title_list,
    "цена": price_list,
    "количество": quantity_list,
    "ед": unit_measure_list
}

print(prod_dict)

print(product_list)
