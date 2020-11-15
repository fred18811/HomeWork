"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, 
открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
dic ={
    "One":"Один",
    "Two":"Два",
    "Three":"Три",
    "Four":"Четыре",
    }
str=""

with open("files/work4.txt", "r", encoding="utf-8") as f:
    for line in f:
        list = line.split()
        list[0]=dic[list[0]]
        str += " ".join(list)+"\n"


with open("files/work4_new.txt", "w") as f:
        f.write(str)
        print(str)