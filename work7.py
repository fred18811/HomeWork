def fact(val):
    for i in range(1,val+1):
        yield i


value = int(input("Введите число: "))
val_fact = 1

for el in fact(value):
    val_fact *= el

print(val_fact)