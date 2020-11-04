my_list = [7, 5, 3, 3]
while True:
    try:
        value = int(input("Введите натурально число положительное или для выхода 'q': "))
        if value < 0:
            raise ValueError
        else:
            break
    except  ValueError:
        print("Вы ввели не положительное число!")


for key,val in enumerate(my_list):
    if val == value:
        my_list.insert(key,value)
        break
    elif value > val:
        my_list.insert(key,value)
        break
    elif len(my_list)-1 == key:
        my_list.append(value)
        break

print(my_list)