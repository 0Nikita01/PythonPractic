print("Задача 2.3. Вводятся три разных числа. Найти, какое из них является средним")

print ("Введите три числа.")

a = float(input("Введите 1 число: "))
b = float(input("Введите 2 число: "))
c = float(input("Введите 3 число: "))

if a >= b and a <= c or a >= c and a <= b:
    print(f"Среднее число: {a}")
elif b >= a and b <= c or b >= c and b <= a:
    print(f"Среднее число: {b}")
else:
    print(f"Среднее число: {c}")