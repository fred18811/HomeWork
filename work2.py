sec = int(input("Введите время в секундах: "))

minutes = sec//60
if minutes > 60:
    minutes = minutes%60

hours = sec//3600
if hours > 24:
    hours = hours%24

sec = sec%60

print("Время - {:02d}:{:02d}:{:02d}".format(hours, minutes, sec))