list =[]
exit = None

def SumList(lst_int,str):
    """
        Функция принимает список и строку.
        Проверяет строку на наличие чисел и символ q
        Возвращает новый список сложенный из списка и чисел из строки
        Возвращает символ q, если он есть
    """
    ext = None
    str = str.split()

    for i in str:
        if i.isdigit():
            lst_int.append(int(i))
        elif i == "q":
            ext = "q"
    return lst_int,ext

while True:
    str = input("Введите числа через пробел или q для выхода: ")
    list,exit = SumList(list,str)
    print(f"Сумма спаска {list} = ",sum(list))

    if exit:
        print("Вы ввели q, программа завершена!")
        break