print("Задача 2.10.")

x = float(input("Введите x: "))

if x > 0:
    print("y =", 2 * x - 10)
elif x == 0:
    print("y =", x)
else:
    print("y =", 2 * abs(x) - 1)