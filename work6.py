def int_func(str):
    """
    Фенкция принимает строку и возвращает строку, 
    где все слова с заглавнами буквами.
    """
    str = str.split()
    count = 0
    while count < len(str):
        str[count] = str[count][0].upper()+ str[count][1:]
        count += 1
    return " ".join(str)

print(int_func(input("Введите строку: ")))