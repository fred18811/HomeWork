def my_func(a,b,c):
    list = [a,b,c]
    list.remove(min(list))
    return sum(list)

print(my_func(11,5,7))