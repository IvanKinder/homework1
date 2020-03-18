sec = int(input("Введите время в секундах: "))

hour = sec // 3600

min = (sec % 3600) // 60

sec = (sec % 3600) % 60

print(f"{hour}:{min}:{sec}")