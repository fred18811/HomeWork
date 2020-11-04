some_str = input("Введите строку: ").split(" ")
for key,val in enumerate(some_str):
    print(key+1,val[:10])