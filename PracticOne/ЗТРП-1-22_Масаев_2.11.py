print("Задача 2.11.")

x = float(input("Введите x: "))

if x < -1:
    print("y =", 1 / (x * x))
elif -1 <= x < 2:
    print("y =", x * x)
else:
    print("y =", 4)