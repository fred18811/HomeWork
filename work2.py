str = input("Введите список значений через запятую или пробел: ")
some_list = str.replace(","," ").split(" ")
some_list = [i for i in some_list if i != ""]

print("Список",some_list)


for key,val in enumerate(some_list):
    if key%2 == 1:
        some_list[key-1],some_list[key] = some_list[key],some_list[key-1]

print("Cписок",some_list)
