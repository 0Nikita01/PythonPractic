print("Задача 2.13.")

n = int(input("Введите порядковый номер дня недели: "))

days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]

if (1 <= n <= 7):
    print(days[n - 1])
else:
    print("Такого порядкого номера нет")