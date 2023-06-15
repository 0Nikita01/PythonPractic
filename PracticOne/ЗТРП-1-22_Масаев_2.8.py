print("Задача 2.8.")

allMarks = int(input("Введите общее количество оценок: "))
perfect = int(input("Введите количество 5: "))
good = int(input("Введите количество 4: "))

if perfect == allMarks:
    print("Стипендия = 6000")
elif good + perfect == allMarks:
    if good == 1:
        print("Стипендия = 4500")
    elif good == 2:
        print("Стипендия = 3750")
    else:
        print("Стипендия = 3000")
else:
    print("Нет стипендии")

