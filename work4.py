while True:
    try:
        numb = int(input("Введите целое положительное число:"))
        if  numb < 0:
            raise ValueError()
        break
    except ValueError:
        print("Выввели не целое положительное число!")


count = 0
maxnumb = 0
strNumber = str(numb)


while count < len(strNumber):
    if int(strNumber[count]) > maxnumb:
        maxnumb = int(strNumber[count])

    count+=1


print(f"Вы ввели число {numb}")
print(f"Самая большая цифра: {maxnumb}")