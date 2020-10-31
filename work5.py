earnings = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))


if earnings > costs:
    print("Прибыль {}".format(earnings-costs))
    print("Рентабельность {}%".format(((earnings-costs)/earnings)*100))
    numpPers = int(input("Введите число сотрудников: "))
    print("Прибыль на доно сотрудника {}".format((earnings-costs)/numpPers))
elif earnings < costs:
    print("Убыток {}".format(earnings-costs))