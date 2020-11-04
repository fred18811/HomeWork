while True:
    try:
        number_month = int(input("Введите мемсяц от 1 до 12: "))
        if number_month < 1 or number_month > 12:
            raise ValueError
        else:
            break
    except  ValueError:
        print("Не число от 1 до 12! Попробуйте сново!")

#dict
month = {
    "Зима":[12,1,2],
    "Весна":[3,4,5],
    "Лето":[6,7,8],
    "Осень":[9,10,11],
}
for key,val in month.items():
    if(val.count(number_month)):
        print(f"Вы ввели {number_month}: время года {key}")
        break

#list
month = [["Зима",12,1,2],["Весна",3,4,5],["Лето",6,7,8],["Осень",9,10,11]]
for val in month:
    if(val.count(number_month)):
        print(f"Вы ввели {number_month}: время года {val[0]}")