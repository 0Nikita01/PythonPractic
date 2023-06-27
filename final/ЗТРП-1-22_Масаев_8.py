#Задача 1
print('''Дано целое число N (> 0). Сформировать и вывести целочисленный
список размера N, содержащий N первых положительных нечетных
чисел: 1, 3, 5, … .''')

N = int(input("Введите целое положительное число N: "))
num = 1
count = 0
lst = []

while count < N:
    lst.append(num)
    num += 2
    count += 1

print("Ответ: ", end = '')
for item in lst:
    print(item, end = ' ')

#----------------------------------------------------------------------------------------------------------------
#Задача 3
print('''Даны целые числа N (> 2), A и B. Сформировать и вывести
целочисленный список размера N, первый элемент которого равен
A, второй равен B, а каждый последующий элемент равен сумме
всех предыдущих.''')

N = int(input("Введите целое число N > 2: "))
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
num = 1
sum = A + B
lst = [A, B]

for i in range(0, N):
    lst.append(sum)
    sum += sum

print("Ответ: ", end = '')
for item in lst:
    print(item, end = ' ')

#----------------------------------------------------------------------------------------------------------------
#Задача 5
from random import randint
print('''Дан целочисленный список размера N. Вывести все содержащиеся
в данном списке четные числа в порядке убывания их индексов, а
также их количество K.''')

N = int(input("Введите целое число N: "))
lst = []

print("\nСгенерированный список: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lst.append(num)
    print(num, end = ' ')
print()

print("Ответ: ", end = '')
for item in lst[::-1]:
    if item % 2 == 0: print(item, end = ' ')

#----------------------------------------------------------------------------------------------------------------
#Задача 6
from random import randint
print('''Дан список A размера N (N — четное число). Вывести его элементы
с четными номерами в порядке возрастания номеров: A2, A4, A6, …,
AN. Условный оператор не использовать.
''')

N = int(input("Введите целое число N: "))
lst = []

print("\nСгенерированный список: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lst.append(num)
    print(num, end = ' ')
print()

print("Ответ:")

#Если выводить элементы с четной позицией в списке:
print("Элементы с четной позицией: " , end = '')
for item in lst[1::2]:
    print(item, end = ' ')

#----------------------------------------------------------------------------------------------------------------
#Задача 8
from random import randint
print('''Дан список размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти
сумму элементов списка с номерами от K до L включительно
''')

N = int(input("Введите целое число N: "))
K = int(input("Введите целое число K: "))
L = int(input("Введите целое число L: "))
lst = []
sum = 0

print("\nСгенерированный список: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lst.append(num)
    print(num, end = ' ')
print()

for item in lst[K:L]:
    sum += item

print("Ответ: ", sum)

#----------------------------------------------------------------------------------------------------------------
#Задача 11
from random import randint
print('''Дан список A размера N. Найти минимальный элемент из его
элементов с четными номерами: A2, A4, A6, … .
''')

N = int(input("Введите целое число N: "))
lst = []

print("\nСгенерированный список: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lst.append(num)
    print(num, end = ' ')
print()

min = lst[1]
for item in lst[1::2]:
    if item < min:
        min = item

print("Ответ: ", min)

#----------------------------------------------------------------------------------------------------------------
#Задача 14
from random import randint
print('''Даны два списка A и B одинакового размера N. Сформировать новый
список C того же размера, каждый элемент которого равен
максимальному из элементов списков A и B с тем же индексом.
''')

N = int(input("Введите целое число N: "))
lstA = []
lstB = []
lstC = []

for i in range(0, N):
    numA = randint(0, 100)
    numB = randint(0, 100)
    lstA.append(numA)
    lstB.append(numB)

print("\nСгенерированный список A: ", end = '')
[print(item,  end = ' ') for item in lstA]

print("\nСгенерированный список B: ", end = '')
[print(item,  end = ' ') for item in lstB]

for i, item in enumerate(lstA):
    lstC.append(max(item, lstB[i]))

print("\nОтвет: список C: ", end = '')
[print(item,  end = ' ') for item in lstC]

#----------------------------------------------------------------------------------------------------------------
#Задача 15
from random import randint
print('''.Дан целочисленный список A размера N. Переписать в новый
целочисленный список B все четные числа из исходного списка (в
том же порядке) и вывести размер полученного списка B и его
содержимое.

''')

N = int(input("Введите целое число N: "))
lstA = []
lstB = []
size = 0

print("\nСгенерированный список: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lstA.append(num)
    print(num, end = ' ')
print()

for item in lstA:
    if (item % 2 == 0):
        lstB.append(item)
        size += 1

print("Ответ: ")
print(f"Размер списка В:", size)
print("Список B: ", end = '')
[print(item,  end = ' ') for item in lstB]

#----------------------------------------------------------------------------------------------------------------
#Задача 20
from random import randint
print('''Дан список A размера N и целое число K (1 ≤ K ≤ N). Преобразовать
список, увеличив каждый его элемент на исходное значение
элемента AK.

''')

N = int(input("Введите целое число N: "))
K = int(input("Введите K: "))
lstA = []

print("\nСгенерированный список A: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lstA.append(num)
    print(num, end = ' ')
print()

Ak = lstA[K]
for i, item in enumerate(lstA):
    lstA[i] += Ak

print("Преобразованный список А: ", end = '')
[print(item,  end = ' ') for item in lstA]

#----------------------------------------------------------------------------------------------------------------
#Задача 22
from random import randint
print('''Дан список размера N. Обнулить элементы списка, расположенные
между его минимальным и максимальным элементами (не включая
минимальный и максимальный элементы).
''')

N = int(input("Введите целое число N: "))
lstA = []


print("\nСгенерированный список A: ", end = '')
for i in range(0, N):
    num = randint(0, 100)
    lstA.append(num)
    print(num, end = ' ')
print()

minA = 0
maxA = 0

for i, item in enumerate(lstA):
    if item < lstA[minA]:
        minA = i
    if item > lstA[maxA]:
        maxA = i

for i, item in enumerate(lstA):
    if i > minA and i < maxA or i < minA and i > maxA:
        lstA[i] = 0

print("Ответ: ", end = '')
[print(item,  end = ' ') for item in lstA]

#----------------------------------------------------------------------------------------------------------------