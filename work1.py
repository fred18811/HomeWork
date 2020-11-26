"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода.
  Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
  Проверить работу полученной структуры на реальных данных.
"""


class InvalidNumber(Exception):
    def __init__(self, text):
        self.txt = text


class Data:
    list_data = []

    def __init__(self, data: "день-месяц-год"):
        Data.__data = data

    @classmethod
    def get_number(cls):
        Data.list_data = [int(i)for i in cls.__data.split("-")]

    @staticmethod
    def valid_number():
        try:
            if not (Data.list_data[0] > 0 and Data.list_data[0] <= 31):
                raise InvalidNumber("Неверный день")
            if not (Data.list_data[1] > 0 and Data.list_data[1] <= 12):
                raise InvalidNumber("Неверный месяц")
            if not (Data.list_data[2] > 0 and Data.list_data[2] <= 2020):
                raise InvalidNumber("Неверный год")
        except InvalidNumber as e:
            print(e)


today_data = Data("31-13-2020")
today_data.get_number()
today_data.valid_number()
