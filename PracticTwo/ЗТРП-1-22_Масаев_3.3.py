print('''Составить алгоритм вывода таблицы перевода перевода 1, 2,...
20 долларов США в рубли по текущему курсу (значение курса вводится
пользователем, ответ выдается столбцом, например, 1 $ = 65 руб.). ''')

exchange = float(input("Введите курс доллара в рублях: "))

for value in range(1, 21):
    print(f"{value} $ =", value * exchange, "руб.")