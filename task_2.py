my_list = input("Введите элементы для списка: ")
my_list = my_list.replace(",", "").replace(".", "").split()

len_list = len(my_list)

print(my_list, id(my_list))

while len_list > 0:
    if len_list > 1:
        my_list.append(my_list.pop(1))
        my_list.append(my_list.pop(0))
        len_list -= 2
    else:
        my_list.append(my_list.pop(0))
        break

print(my_list, id(my_list))
