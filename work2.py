from abc import ABC, abstractmethod


class ABC_Сlothes(ABC):
    @abstractmethod
    def get_size_fabric(self):
        print("Расчитать размер ткани")


class Сlothes(ABC_Сlothes):
    __count_fabric = 0
    __count_coat = 0
    __count_suit = 0

    def __init__(self, clothes_type, size_val):
        self.__clothes_type = clothes_type          # Тип вещи (пальто ил костюм)
        self.__size_val = size_val                  # Размер вещи
        try:
            if self.__clothes_type == "пальто":     # Колличество ткани для определенного типа
                self.__val_fabric = self.__size_val/6.5 + 0.5
                Сlothes.__count_coat += 1
            elif self.__clothes_type == "костюм":
                self.__val_fabric = 2 * self.__size_val + 0.3
                Сlothes.__count_suit += 1
            else:
                raise TypeError
        except TypeError:
            print("Нет такого типа одежды")
        Сlothes.__count_fabric += self.__val_fabric

    def get_size_fabric(self):
        return self.__val_fabric

    @property
    def count_fabric(self):
        return f"Общее колличество материала - {round(Сlothes.__count_fabric, 2)}\n Пальто - {Сlothes.__count_coat}шт\n Костюм - {Сlothes.__count_suit}шт"

    @property
    def info_clothes(self):
        return f"Тип одежды '{self.__clothes_type}'\nРазмер {self.__size_val}"


coat1 = Сlothes("пальто", 50)
print("_"*100)
coat2 = Сlothes("пальто", 40)
print(coat1.get_size_fabric())
print("_"*100)
print(coat2.info_clothes)
print("_"*100)
suit1 = Сlothes("костюм", 170)
print(suit1.get_size_fabric())
print("_"*100)
print(suit1.count_fabric)
