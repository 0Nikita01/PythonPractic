import math
print("Задача 2.12.")

x = float(input("Введите x: "))
y = float(input("Введите y: "))

z = None

if x + y < 2:
    z = math.sqrt(x*x + y*y)
elif x + y == 3 or x + y == 8:
    z = 2*x*y
elif x + y >= 10:
    z = x - y
else:
    z = 2*x + 3*y

u = 3*z*z - 2*z + 5

print("Ответ: u =", u)

