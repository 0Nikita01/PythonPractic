print("Задача 4.4.")

n = int(input("Введите натуральное число n: "))

if n > 1:
    copyN = n
    


    while copyN > 1:
        copyN -= 1
        print(copyN, end = ' ')
elif n == 1:
    print(f"Натуральных чисел меньше {n} нет")
else:
    print(f"Число {n} не является натуральным!")