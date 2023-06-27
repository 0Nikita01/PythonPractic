import math
print(''' Найти сумму и произведение цифр n-значного числа, которое
вводит пользователь.''')

n = input("Введите число n: ")

sum = 0
multi = 1

if '.' in n:
    n = n.replace('.', '')
    n = int(n)
else:
    n = int(n)

n = abs(n);

while n > 0:
    digit = n % 10
    sum += digit
    multi *= digit

    n //= 10

if (sum == 0):
    multi = 0

print(f"Ответ:\nСумма цифр = {sum}\nПроизведение цифр = {multi}")
