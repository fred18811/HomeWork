"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

# Выбрасывает ошибку если такого оборудования нет
class NotSellectEqu(Exception):
    def __init__(self, err):
        self.err = err


# Определяем класс склад
class Warehouse:
    def __init__(self):
        self.__units = {
            "printer": [],
            "scaner": [],
            "сopier": [],
        }

    # Добавляем оборудование на склад
    def set_equ_on_warehouse(self, obj):
        try:
            if isinstance(obj, Printe):
                self.__units["printer"].append({
                    "obj": obj,
                    "depart": "",
                    "instal": False,
                })
            elif isinstance(obj, Scaner):
                self.__units["scaner"].append({
                    "obj": obj,
                    "depart": "",
                    "instal": False,
                })
            elif isinstance(obj, Сopier):
                self.__units["сopier"].append({
                    "obj": obj,
                    "depart": "",
                    "instal": False,
                })
            else:
                raise NotSellectEqu(
                    "При добавлении на склад - нет такого устройства")
        except NotSellectEqu as err:
            print(err, obj)

    # Добавляем оборудование в отдел
    def set_equ_on_depart(self, type_equ: "scaner, printer, copier", name: "name equ", depart):
        try:
            for i in self.__units[type_equ]:
                if i["obj"].get_param_eqi()["name"] == name:
                    print(name)
                    i["depart"] = depart
                    i["instal"] = True
                    return True
            raise NotSellectEqu("При добавлении в департамент - нет такого устройства")
        except NotSellectEqu as err:
            return (err, type_equ)

    # Информация по оборудованию
    def __get_info_equ(self, type_equ):
        if len(self.__units[type_equ]):
            str_equ = ""
            for i in self.__units[type_equ]:
                name = i["obj"].get_param_eqi()["name"]
                if i["instal"]:
                    str_equ = str_equ + f"{name}, установлен {i['depart']}\n"
                else:
                    str_equ = str_equ + f"{name}, на складе\n"
            return str_equ

    # Получение колличество устройст
    def __get_count_equ(self, type_equ):
        return len(self.__units[type_equ])

    # Вывод статичтики по оборудованию
    def get_info_warehouse(self, type_equ):
        return f"Всего {type_equ} {self.__get_count_equ(type_equ)}\n\n {self.__get_info_equ(type_equ)}"
    
    # Вывод информации устройст на складе
    def get_free_que(self, type_equ):
        if len(self.__units[type_equ]):
            str_equ = ""
            for i in self.__units[type_equ]:
                name = i["obj"].get_param_eqi()["name"]
                if not i["instal"]:
                    str_equ = str_equ + f"{name}, на складе\n"
            if str_equ:
                return str_equ
            else:
                return


# Базовый класс
class OfficeEquipment:
    def __init__(self, name, paper_format, interface: "[usb,lan,lpt,com,wifi]", color: "type boole", duplex: "type boole", sn: "serial number"):
        self.unit = {
            "sn":sn,
            "name": name,
            "paper_format": paper_format,
            "interface": interface,
            "color": color,
            "duplex": duplex,
        }

    def get_param_eqi(self):
        return self.unit


class Printe(OfficeEquipment):
    def __init__(self, name, speed_print, type_print: "laser or jet", paper_format, interface: "[usb,lan,lpt,com,wifi]", color: "type boole", duplex: "type boole", sn: "serial number"):
        super().__init__(name, paper_format, interface, color, duplex, sn)
        self.unit["speed_print"] = speed_print
        self.unit["type_print"] = type_print


class Scaner(OfficeEquipment):
    def __init__(self, name, speed_scaner, type_scaner: "tablet or streaming", paper_format, interface: "[usb,lan,lpt,com,wifi]", color: "type boole", duplex: "type boole", sn: "serial number"):
        super().__init__(name, paper_format, interface, color, duplex, sn)
        self.speed_scaner = speed_scaner
        self.type_scaner = type_scaner


class Сopier(OfficeEquipment):
    def __init__(self, name, speed_сopier, paper_format, interface: "[usb,lan,lpt,com,wifi]", color: "type boole", duplex: "type boole", sn: "serial number"):
        super().__init__(name, paper_format, interface, color, duplex, sn)
        self.speed_сopier = speed_сopier
