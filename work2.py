"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
 При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivOnZero(ZeroDivisionError):
    def __init__(self, text):
        self.txt = text


class DivNumb:
    @staticmethod
    def div_numb(numb1, numb2):
        try:
            if numb2:
                return numb1/numb2
            else:
                raise DivOnZero("Попытка деления на ноль")
        except DivOnZero as e:
            return e


print(DivNumb.div_numb(12, 0))
