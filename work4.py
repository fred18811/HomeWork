while True:
    x = int(input("Введите положителтное число: "))
    if x >= 0:
        break

while True:
    y = int(input("Введите отрицательное число: "))
    print(y)
    if y < 0:
        break

def my_func(x, y):
    #Первый способ
    print(f"Число {x} возведенное в степень {y} равно ",x**y)

    #Второй способ
    count = 1
    z = x
    while count<abs(y):
        z*=x
        count+=1
    if y<0:
        z = 1/z
    print(f"Число {x} возведенное в степень {y} равно ",z)


my_func(x,y)