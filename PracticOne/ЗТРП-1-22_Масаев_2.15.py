print("Задача 2.15.")

m = int(input("Введите m: "))
n = int(input("Введите n: "))

if m == n:
    m = 0
    n = 0
elif m > n:
    n = m
else:
    m = n

print(f"Ответ: m = {m}, n = {n}")