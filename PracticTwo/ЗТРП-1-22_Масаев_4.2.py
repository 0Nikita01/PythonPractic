print("Задача 4.2.")

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

if a < b:
    print(f"Ответ: Числа между {a} и {b}: ", end = '')

    if b - a == 1:
        print("Таких чисел нет")
    else:
        while b > a + 1:
            b -= 1
            print(b, end = " ")   
else:
    print("A должно быть меньше B!")
