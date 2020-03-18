n = int(input("Введите натуральное число: "))
max = 0
i = 0

while i < len(str(n)):
    if (n // (10 ** i)) % 10 > max:
        max = (n // (10 ** i)) % 10
    i += 1
print(max)
