print("Задача 3.10.")

n = int(input("Введите число n: "))

sum = 0

if n <= 0:
    print("Число n должны быть натуральными!")
else:
    for k in range(1, n + 1):
        sum += (2*k - 1) / (k + 1)

    print("Ответ: Сумма =", sum)

