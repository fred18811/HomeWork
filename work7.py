"""
7. Создать (не программно) текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, 
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, 
вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

list = []
with open("files/work7.txt", "r", encoding="utf-8") as f:
    dic = {}
    average_profit = 0
    count = 0
    for line in f:
        firma,*state = line.split()
        costs = [int(i) for i in state if i.isdigit()]
        average  = costs[0]-costs[1]
        if average >= 0:
            average_profit += average
            count += 1
        dic[firma] = average
    list.append(dic)
    list.append({"average_profit":average_profit/count})


with open("files/work7.json", "w") as jsn:
    json.dump(list, jsn)