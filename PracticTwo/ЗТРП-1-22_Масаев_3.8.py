print('''Дано натуральное число n. Вычислить произведение и
количество четных цифр числа.''')

n = input("Введите натуральное число n: ")

#1 вариант решения
evenMulti = 1
evenQuantity = 0
nToInt = int(n);


if (nToInt <= 0):
    print(f"Число {nToInt} не является натуральным")
else:
    for digit in n:
        digitToInt = int(digit)
        
        if digitToInt % 2 == 0:
            evenMulti *= digitToInt
            evenQuantity += 1
    
if evenQuantity == 0:
    evenMulti = 0

print("Ответ:")
print(f"Произведение четных цифр числа {nToInt} = {evenMulti}")
print(f"Количество четных цифр числа {nToInt} = {evenQuantity}")


#Есть другой метод: путем взятия остатка при делении числа на 10
#И после отрезаем последнюю цифру числа и так пока не дойдет до 1 разряда 
# Код ниже

#2 вариант решения

# length = len(n)
# evenMulti = 1
# evenQuantity = 0
# nToInt = int(n);

# if (nToInt <= 0):
#     print(f"Число {nToInt} не является натуральным")

# for i in range(1, length + 1):
#     digit = nToInt % 10

#     if digit % 2 == 0:
#             evenMulti *= digit
#             evenQuantity += 1

#     nToInt //= 10

# if evenQuantity == 0:
#     evenMulti = 0

# print("Ответ:")
# print(f"Произведение четных цифр числа {n} = {evenMulti}")
# print(f"Количество четных цифр числа {n} = {evenQuantity}")