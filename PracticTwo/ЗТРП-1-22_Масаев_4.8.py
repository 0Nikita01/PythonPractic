print("Задача 4.8.")

n = int(input("Введите целое число n: "))

n = abs(n)
kolDigits = 0

if n == 0:
    kolDigits += 1

while n > 0:
    n //= 10
    kolDigits += 1

print(f"Ответ: {kolDigits}")