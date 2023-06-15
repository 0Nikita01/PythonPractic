print("Задача 4.9.")

n = 1
sumOfOddNumbers = 0

while n < 100:
    if n % 2 != 0:
        sumOfOddNumbers += n
    n += 1

print("Ответ: Сумма нечетных чисел от 1 до 99 = ", sumOfOddNumbers)