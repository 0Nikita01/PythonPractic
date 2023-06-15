print("Задача 3.3.")

exchange = float(input("Введите курс доллара в рублях: "))

for value in range(1, 21):
    print(f"{value} $ =", value * exchange, "руб.")