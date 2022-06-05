my_list = input("Введите слова через пробел: ")

my_list = my_list.title().replace(",", "").replace(".", "").split()

for i, v in enumerate(my_list, 1):
    print(f"{i}) {v[:10]}")