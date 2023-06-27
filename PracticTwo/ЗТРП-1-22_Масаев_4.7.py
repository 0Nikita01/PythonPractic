print("Найти все целые числа до 200, сумма которых равна 13.")

number = 1
i = 0

print("Ответ:")

while number < 200:
    numberCopy = number
    sumOfDigits = 0

    while numberCopy > 0:
        sumOfDigits += numberCopy % 10
        numberCopy //= 10
    
    if sumOfDigits == 13:
        print(number, end = ' ')
        i += 1
    if i == 5:
        i = 0
        print()
    
    number += 1