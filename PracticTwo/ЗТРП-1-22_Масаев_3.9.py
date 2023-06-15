print("Задача 3.9.")

n = int(input("Введите число n: "))

sum = 0

if n <= 0:
    print("Число n должны быть натуральными!")
else:
    for k in range(1, n + 1):
        sum += 1 / (k ** 5)

    print("Ответ: Сумма =", sum)
