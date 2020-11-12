from functools import reduce

list = [val for val in range(100,1000) if not val%2]
print(f"Список четных чисел от 100 до 1000 {list}")
print(reduce(lambda x, y: x*y, list))