print("Задача 4.6.")

n = input("Введите натуральное число n: ")
length = len(n)
n = int(n)

multi = 1
kol = 0

if (n > 0):
    while n > 0:
        if length % 2 != 0:
            multi *= n % 10
            kol += 1
        n //= 10
        length -= 1
        
    print(f"Ответ:\nПроизвдение нечетных цифр: {multi}\nКоличество нечетных цифр: {kol}")

else:
    print(f"Число {n} не натуральное!")
