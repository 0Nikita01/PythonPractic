print('''Дана следующая функция y=f(x):
y = 2x - 10, если x > 0
y = 0, если x = 0
y = 2 * |x| - 1, если x < 0
Требуется найти значение функции по переданному x (вводится
пользователем).''')

x = float(input("Введите x: "))

if x > 0:
    print("y =", 2 * x - 10)
elif x == 0:
    print("y =", x)
else:
    print("y =", 2 * abs(x) - 1)