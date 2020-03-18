dohod = float(input("Введите значение выручки: "))
trata = float(input("Введите значение издержек: "))

if dohod > trata:
    rent = dohod / trata
    print("Прибыль.\n", f"Рентабельность = {rent}")
    population = int(input("Введите численность сотрудников: "))
    print("Прибыль на одного сотрудника составляет: ", (dohod - trata) / population)
else:
    print("Убыток")
