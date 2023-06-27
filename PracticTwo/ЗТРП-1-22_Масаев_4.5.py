import math

print('''Дано число n. Составить алгоритм поиска первого натурального
числа, квадрат которого больше n.''')

n = float(input("Введите число n: "))

if n < 1:
    print("Ответ: 1")
else:
    sn = math.sqrt(n)
    print("Ответ:", math.floor(sn) + 1) 
