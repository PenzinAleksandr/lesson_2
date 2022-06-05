my_list = [7, 5, 3, 3, 2]
my_list.reverse()
num = int(input("Введите число: "))

len_list = len(my_list)

for i in my_list:
    if num > i and num not in my_list:
        my_list.append(num)
        break
    elif num < i and num not in my_list:
        my_list.insert(0, num)
        break
    elif num == i:
        temp_idx = my_list.index(num)
        my_list.insert(temp_idx, num)
        break
my_list.reverse()
print(my_list)