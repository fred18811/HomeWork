"""
7. Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, val1, val2):
        self.__val1 = val1
        self.__val2 = val2

    def __add__(self, other):
        return ComplexNumber(self.__val1 + other.__val2, self.__val2 + other.__val2)

    def __mul__(self, other):
        return ComplexNumber(self.__val1 * other.__val1, self.__val2 * other.__val2)

    def __str__(self):
        return f"({self.__val1},{self.__val2})"


val1 = ComplexNumber(1, 2)
val2 = ComplexNumber(6, 6)
print(val1)
print(val1 + val2)
print(val1*val2)
