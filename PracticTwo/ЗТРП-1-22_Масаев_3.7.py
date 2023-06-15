print("Задача 3.7.")

sum = 0

for number in range(1, 100):
    if number % 2 != 0:
        sum += number

print("Сумма нечетных чисел от 1 до 99 =", sum)