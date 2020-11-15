"""
3. Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
with open("files/work3.txt","a+") as f:
	while True:
		str = input("Введите фамилию сотрудника и оклад!Для выхода введите 'q или й': ")
		if str == "q" or str == "й":
			break
		else:
			f.write(f"{str}\n")


salary = 0
count = 0
s_name ="\n"
with open("files/work3.txt","r") as f:
		for line in f:
			name,cost = line.split()
			if int(cost) < 20000:
				s_name += line
			salary += int(cost)
			count += 1

print(f"Сотрудники у кого зп меньше 20тыс: {s_name}")
print("Срезняя зп сотрудников: {}".format(salary/count))