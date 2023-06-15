print("Задача 3.4.")

price = float(input("Введи цену за 1 кг конфет: "))
maxLength = len(str(price * 10)) + 14
underAndBottomLine = ""

for symbol in range(maxLength):
        underAndBottomLine += "_"

print(underAndBottomLine);

for value in range(2, 11):
    result = value * price

    if value == 10:
        print(f" {value} кг | {result} руб")
    else:
        print(f" {value} кг  | {result} руб")
    
    print(underAndBottomLine);