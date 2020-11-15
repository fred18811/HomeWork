"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open("files/work2.txt","r", encoding="utf-8") as f:
    count = 0
    for line in f:
        count += 1
        print("Строка {}, колличество слов {}".format(count,len(line.split(" "))))

    print(f"Колличество строк {count}")