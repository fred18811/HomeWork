from sys import argv

name, production, rate, prize = argv
print("Зарплата сотрудника",(int(production)*int(rate))+int(prize))