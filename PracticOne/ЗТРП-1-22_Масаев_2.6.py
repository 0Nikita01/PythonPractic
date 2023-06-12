print("Задача 2.6. Дано трехзначное натуральное число.\nВычислить произведение ненулевых цифр этого числа\n")

num = int(input("Введите трехзначное натуральное число: "))

multi = 1
buffer = num % 10

multi *= buffer if buffer != 0 else 1

buffer = num // 10 % 10
multi *= buffer if buffer != 0 else 1

buffer = num // 100
multi *= buffer if buffer != 0 else 1

print(f"Произведение ненуливых цифр числа {num} = {multi}")