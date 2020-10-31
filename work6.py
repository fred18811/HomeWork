a = int(input("Первый день спортсмен пробежал (км): "))
b = int(input("Общий результат (км): "))
count = 1
while True:
    if b <= a:
        print("День\дней {}".format(count))
        break

    a = a*1.1
    count+=1