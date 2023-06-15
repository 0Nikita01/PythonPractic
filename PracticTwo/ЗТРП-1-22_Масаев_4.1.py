print("Задача 4.1.")

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

if a < b:
    print(f"Ответ: Числа между {a} и {b}: ", end = '')

    if b - a == 1:
        print("Таких чисел нет")
    else:
        while a < b - 1:
            a += 1
            print(a, end = " ")     
else:
    print("A должно быть меньше B!")
