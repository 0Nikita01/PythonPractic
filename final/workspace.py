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