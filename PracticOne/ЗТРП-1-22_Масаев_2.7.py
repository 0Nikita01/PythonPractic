print("Задача 2.7.")

V1 = float(input("Введите первое значение скорости в км/ч: "))
V2 = float(input("Введите второе значение скорости в м/с: "))

V1ms = V1 / 3.6

if (V1ms > V2):
    print(f"{V1} км/ч > {V2} м/с")
elif (V1ms < V2):
    print(f"{V2} м/с > {V1} км/ч")
else:
    print(f"{V1} км/ч = {V2} м/с")