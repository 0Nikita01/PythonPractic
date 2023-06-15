import math

print("Задача 4.5.")

n = float(input("Введите число n: "))

if n < 1:
    print("Ответ: 1")
else:
    sn = math.sqrt(n)
    print("Ответ:", math.floor(sn) + 1) 
