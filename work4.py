"""
4. Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""
class Car:
    __is_police = False

    def __init__(self,speed,color,name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")
        print("_"*100)

    def stop(self):
        print("Машина остановилась")
        print("_"*100)

    def turn(self,direction):
        print("Машина повернула",direction)
        print("_"*100)

    def show_speed(self):
        print("Скорость автомобиля ",self.speed)
        print("_"*100)

    def get_status_auto(self):
        if Car.__is_police:
            print("Машина полицейская")
            print("_"*100)
        else:
            print("Гражданиский автомобиль")
            print("_"*100)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена на ",abs(60-self.speed))
            print("_"*100)
        else:
           print("Скорость автомобиля ",self.speed)
           print("_"*100)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена на ",abs(60-self.speed))
            print("_"*100)
        else:
            print("Скорость автомобиля ",self.speed)
            print("_"*100)


class PoliceCar(Car):
    __is_police = True

    def get_status_auto(self):
        if PoliceCar.__is_police:
            print("Машина полицейская")
            print("_"*100)
        else:
            print("Гражданиский автомобиль")
            print("_"*100)


class SportCar(Car):
    pass


fiat = TownCar(40,"черный","Fiat Panda")
bugatti = SportCar(100,"красный","BUGATTI Veyron")
kamaz = WorkCar(60,"оранжевый","KAMAZ")
police = PoliceCar(70,"синий","Ford Focus")

fiat.go()
fiat.turn("налево")
fiat.show_speed()
fiat.speed = 70
fiat.show_speed()
fiat.stop()
police.get_status_auto()
kamaz.get_status_auto()