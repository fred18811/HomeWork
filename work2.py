list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el for key,el in enumerate(list) if el>list[key-1] and key-1 != -1])