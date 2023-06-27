print("Составить алгоритм вывода значений следующих чисел: 2, 4, …,20.")

for value in range(1, 21):
    if (value % 2 == 0):
        print(value, end = ' ')
