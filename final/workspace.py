print('''В данном трехзначном числе переставьте цифры так, чтобы новое число
оказалось наибольшим из возможных.''')

number = int(input("Введите трехзнаное число: "))
newNumber = 0

a = number // 100
b = number // 10 % 10
c = number % 10

if a >= b >= c:
    newNumber = a * 100 + b * 10 + c
elif b >= a >= c:
    newNumber = b * 100 + a * 10 + c 
elif c >= a >= b:
    newNumber = c * 100 + a * 10 + b
elif a >= c >= b:
    newNumber = a * 100 + c * 10 + b
elif b >= c >= a:
    newNumber = b * 100 + c * 10 + a
elif c >= b >= a:
    newNumber = c * 100 + b * 10 + a

print("Ответ: ", newNumber)