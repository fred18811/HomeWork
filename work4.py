"""
6. Продолжить работу над вторым заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from MyClassForWok4 import Warehouse, Printe, Scaner, Сopier


start = "\nВведите число!\n 1 - Добавить новое устройство на склад \n 2 - Перенести устройство в отдел\n 3 - Перенести устройство насклад\n 4 - Посмотреть общую статистику\n 5 - Выйти\n"
addequ = "Какое устойство добавляем?\n 1 - Принтер\n 2 - Сканер\n 3 - Копир\n 4 - Выйти\n"
move_equ_on_depart = "Какое устойство переносим?\n 1 - Принтер\n 2 - Сканер\n 3 - Копир\n 4 - Выйти\n"


#Проверяем введенные данные
def check_input_data(data, res):
    if res == "int":
        if data.isdigit():
            return int(data)
        else:
            return
    elif res == "boole":
        if data == "False" or data == "True":
            return bool(data)
        else:
            return
    elif type(res) is list:
        new_data = []
        data = data.split(",")
        for i in data:
            for j in res:
                if i == j:
                    new_data.append(i)
        if new_data:
            return new_data
        else:
            return


#Цикл ввода данных если данные не верны
def cycle(msg,res):
    while True:
        val = input(msg)
        if check_input_data(val, res):
            return check_input_data(val, res)


#Вводим данные устройства
def input_data_equ(warh,type_equ):
    name = input(f"Введите имя {type_equ} : ")
    speed = cycle(f"Введите скорость {type_equ} : ","int")
    type_form = cycle(f"Введите формат {type_equ}| A3, A4 : ",["A3","A4"])
    interf = cycle(f"Введите тип интерфейсов {type_equ} | через запятую usb,lan,lpt,com,wifi : ",["usb","lan","lpt","com","wifi"])
    duplex = cycle(f"Введите двухстароння печать\сканирование\копирование {type_equ} | True, False : ","boole")
    color = cycle(f"Устройство цветное {type_equ} | True, False : ","boole")
    sn = input(f"Введите серийный номер {type_equ} : ")
    if type_equ == "printer":
        type_print = cycle(f"Тип {type_equ} | color или laser : ",["color","laser"])
        warh.set_equ_on_warehouse(Printe(name, speed, type_print,type_form, interf, color, duplex, sn))
    elif type_equ == "scaner":
        type_scan = cycle(f"Тип {type_equ} | tablet или streaming : ",["tablet","streaming"])
        warh.set_equ_on_warehouse(Scaner(name, speed, type_scan,type_form, interf, color, duplex, sn))
    elif type_equ == "сopier":
        warh.set_equ_on_warehouse(Сopier(name, speed,type_form, interf, color, duplex, sn))


company = Warehouse()
company.set_equ_on_warehouse(Printe("HPLJ1020n", 100, "laser","A4", ["usb,lan"], False, False, "1234"))
company.set_equ_on_warehouse(Printe("HPCLJ5550nd", 500, "laser","A3", ["usb,lan"], True, True, "1235"))
company.set_equ_on_warehouse(Printe("test", 300, "laser","A4", ["usb,lan"], True, True, "125454435"))
company.set_equ_on_warehouse(Scaner("HPScanJet2500", 100, "table", "A4", ["usb"], True, True, "1234"))
company.set_equ_on_warehouse(Сopier("somecopier", 100, "A3", ["usb, lan"], False, False, "1234"))
company.set_equ_on_depart("printer", "HPLJ1020n", "Бухгалтерия")
company.set_equ_on_depart("scaner", "HPScanJet2500", "Бухгалтерия")


while True:
    val = int(input(start))
    print("\n"*100)
    if val == 5:
        break
    elif val == 1:
        while True:
            print("_"*100)
            val = int(input(addequ))
            if val == 1:
                input_data_equ(company,"printer")
            elif val == 2:
                input_data_equ(company,"scaner")
            elif val == 3:
                input_data_equ(company,"сopier")
            elif val == 4:
                break
    elif val == 2:
        while True:
            val = int(input(move_equ_on_depart))
            if val == 1:
                while True:
                    print("\n"*100)
                    print("_"*100)
                    if not company.get_free_que("printer"):
                        print ("Устройств нет на складе")
                        break
                    else:
                        print(company.get_free_que("printer"))
                    print("_"*100)
                    name = input("Какое устройство переносим?\n")
                    depart = input("Куда переносим?\n")
                    company.set_equ_on_depart("printer", name, depart)
                    break
            elif val == 2:
                while True:
                    print("\n"*100)
                    print("_"*100)
                    if not company.get_free_que("scaner"):
                        print ("Устройств нет на складе")
                        break
                    else:
                        print(company.get_free_que("scaner"))
                    print("_"*100)
                    name = input("Какое устройство переносим?\n")
                    depart = input("Куда переносим?\n")
                    company.set_equ_on_depart("scaner", name, depart)
                    break
            elif val == 3:
                while True:
                    print("\n"*100)
                    print("_"*100)
                    if not company.get_free_que("сopier"):
                        print ("Устройств нет на складе")
                        break
                    else:
                        print(company.get_free_que("сopier"))
                    print("_"*100)
                    name = input("Какое устройство переносим?\n")
                    depart = input("Куда переносим?\n")
                    company.set_equ_on_depart("сopier", name, depart)
                    break
            elif val == 4:
                break
    elif val == 3:
        print("Здесь должен был быть перенос из подразделений на склад")
    elif val == 4:
        print("_"*100)
        print(company.get_info_warehouse("printer"))
        print("_"*100)
        print(company.get_info_warehouse("scaner"))
        print("_"*100)
        print(company.get_info_warehouse("сopier"))
