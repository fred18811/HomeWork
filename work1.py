a = int(input("Введите число a: "))
b = int(input("Введите число b: "))


def Div(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Попытка деления на ноль")


Div(a,b)