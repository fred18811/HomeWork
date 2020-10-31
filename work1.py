name = "Tom"
count = 123
stateCount = False

print(f"name {name}")
print("count {}, state {}".format(count,stateCount))


while(True):
    try:
        numb = int(input("Введите число:"))
        break
    except ValueError:
        print("Вы ввели не число!")

str = input("Введите строку:")

print("Ваше число {}".format(numb))
print("Ваша строка {}".format(str))
