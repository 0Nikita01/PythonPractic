#3.4--------------------------------------------------------------------------------------------
print('''Дано трехзначное число. Вывести число, полученное при прочтении
исходного числа справа налево.''')

number = int(input("Введите трехзнаное число: "))
newNumber = 0

newNumber = number % 10 * 100 + number // 10 % 10 * 10 + number // 100

print("Ответ: ", newNumber)

#3.7---------------------------------------------------------------------------------------------
print('''В данном трехзначном числе переставьте цифры так, чтобы новое число
оказалось наибольшим из возможных.''')

number = int(input("Введите трехзнаное число: "))
newNumber = 0

a = number // 100
b = number // 10 % 10
c = number % 10

if a >= b >= c:
    newNumber = a * 100 + b * 10 + c
elif b >= a >= c:
    newNumber = b * 100 + a * 10 + c 
elif c >= a >= b:
    newNumber = c * 100 + a * 10 + b
elif a >= c >= b:
    newNumber = a * 100 + c * 10 + b
elif b >= c >= a:
    newNumber = b * 100 + c * 10 + a
elif c >= b >= a:
    newNumber = c * 100 + b * 10 + a

print("Ответ: ", newNumber)

#3.12--------------------------------------------------------------------------------------------
print("#3.12")
print('''Дано число в двоичной системе. Определите это число в десятичной
системе (в двух вариантах: а) вычисляя математически; б) преобразуя
число из двоичной системы счисления)\n''')

number = input("Введите число в двоичной системе: ")

#1 вариант
numberA = number[::-1]
numberDecA = 0
i = 0

for n in numberA:
    numberDecA += 2**i * int(n)
    i += 1

#2 вариант
numberDecB = int(number, 2)

print(f'''Ответ:
a) {number} = {numberDecA}
б) {number} = {numberDecB}
''')

#3.14--------------------------------------------------------------------------------------------
print("#3.14")
print('''Если сложить все цифры какого-либо натурального числа, затем — все
цифры найденной суммы и так далее, то в результате получим
однозначное число (цифру), которое называется цифровым корнем
данного числа. Например, цифровой корень числа 561 равен 3 (5 + 6+1
— 12, 1+2 = 3). Найдите числовой корень данного натурального числа n.
N вводится пользователем
''')

number = int(input("Введите натуральное число: "))
numcopy = number

sumNumbers = 0
sumNumbersOfSum = 0

while numcopy > 0:
    sumNumbers += numcopy % 10
    numcopy //= 10

while sumNumbers > 0:
    sumNumbersOfSum += sumNumbers % 10
    sumNumbers //= 10

print(f"Ответ: Числовой корень числа {number} = {sumNumbersOfSum}")

#3.15--------------------------------------------------------------------------------------------
print("#3.15")
print('''Номера троллейбусных билетов представляют собой шестизначные
числа. Счастливым считается тот билет, у которого сумма первых цифр
равна сумме трех последних цифр. Например, билет 627 294 считается
счастливым, так как 6 + 2 + 7 = 2 + 9 + 4=15. Найдите все счастливые
комбинации.
''')

ticket = ""
zero = "00000"
i = 0

print("Ответ:")

for n in range(0, 100000):
    strN = str(n)
    if n < 100000:
        ticket = zero[0:6 - len(strN)] + strN
    else:
        ticket = strN

    leftSum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    rightSum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if leftSum == rightSum:
        if i == 30:
            print()
            i = 0
        print(ticket, end = "  ")
        i += 1

#3.16--------------------------------------------------------------------------------------------
print("#3.16")
print('''Б. Кордемский указывает одно интересное число 145, которое равно
сумме факториалов своих цифр: 145=1!+4!+5!. Он пишет, что
неизвестно, есть ли еще такие числа, удовлетворяющие названному
условию. Помогите найти все такие числа.
''')

def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        return number * factorial(number - 1)

n = 1
i = 0

print("Ответ: ")

while n < 10**7:
    sumFacctorials = 0
    strN = str(n)

    for f in strN:
        sumFacctorials += factorial(int(f))
    
    if n == sumFacctorials:
        print(n)

    n += 1

#4.8--------------------------------------------------------------------------------------------
print("4.8")
print('''Даны координаты двух различных полей шахматной доски x1, y1,
x2, y2 (целые числа, лежащие в диапазоне 1–8). Проверить
истинность высказывания: «Данные поля имеют одинаковый цвет»
''')

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("Ответ:", True)
else:
    print("Ответ:", False)

#4.9--------------------------------------------------------------------------------------------
print("4.9")
print(''' Даны координаты двух различных полей шахматной доски x1, y1,
x2, y2 (целые числа, лежащие в диапазоне 1–8). Проверить
истинность высказывания: «Ладья за один ход может перейти с
одного поля на другое».
''')

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if x1 == x2 or y1 == y2:
    print("Ответ:", True)
else:
    print("Ответ:", False)   

#4.16--------------------------------------------------------------------------------------------
'''Арифметические действия над числами пронумерованы следующим образом: 1 — сложение, 2 — вычитание, 3 —умножение, 
4 — деление. Дан номер действия N (целое число в диапазоне 1–4) и вещественные числа A и B (В не равно 0).
Выполнить над числами указанное действие и вывести результат.'''
N = int(input("Введите номер действия (1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление): "))
A = float(input("Введите вещественное число A: "))
B = float(input("Введите вещественное число B: "))
if N == 1:
    result = A + B
elif N == 2:
    result = A - B
elif N == 3:
    result = A * B
elif N == 4:
    result = A / B
else:
    print("Ошибка: некорректный номер действия")
    exit()
print("Результат:", result)

#4.18--------------------------------------------------------------------------------------------
'''Даны координаты двух различных полей шахматной доски x1, y1,x2, y2 (целые числа, лежащие в диапазоне 1–8). Проверить
истинность высказывания: «Конь за один ход может перейти содного поля на другое».'''
x1 = int(input("Введите координату x первого поля: "))
y1 = int(input("Введите координату y первого поля: "))
x2 = int(input("Введите координату x второго поля: "))
y2 = int(input("Введите координату y второго поля: "))
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    print("Конь может перейти с одного поля на другое за один ход")
else:
    print("Конь не может перейти с одного поля на другое за один ход")

#4.19--------------------------------------------------------------------------------------------
'''Локатор ориентирован на одну из сторон света («С» — север, «З» —запад, «Ю» — юг, «В» — восток) и может принимать три цифровые
команды поворота: 1 — поворот налево, –1 — поворот направо, 2— поворот на 180°. Дан символ C — исходная ориентация локатора
и целые числа N1 и N2 — две посланные команды. Вывести ориентацию локатора после выполнения этих команд.'''
C = input("Введите исходную ориентацию локатора (С, З, Ю, В): ")
N1 = int(input("Введите первую команду поворота (-1, 1 или 2): "))
N2 = int(input("Введите вторую команду поворота (-1, 1 или 2): "))
if C == "С":
    if N1 == 1:
        C = "З"
    elif N1 == -1:
        C = "В"
    elif N1 == 2:
        C = "Ю"
    if N2 == 1:
        C = "З"
    elif N2 == -1:
        C = "В"
    elif N2 == 2:
        C = "Ю"
elif C == "З":
    if N1 == 1:
        C = "Ю"
    elif N1 == -1:
        C = "С"
    elif N1 == 2:
        C = "В"
    if N2 == 1:
        C = "Ю"
    elif N2 == -1:
        C = "С"
    elif N2 == 2:
        C = "В"
elif C == "Ю":
    if N1 == 1:
        C = "В"
    elif N1 == -1:
        C = "З"
    elif N1 == 2:
        C = "С"
    if N2 == 1:
        C = "В"
    elif N2 == -1:
        C = "З"
    elif N2 == 2:
        C = "С"
elif C == "В":
    if N1 == 1:
        C = "С"
    elif N1 == -1:
        C = "Ю"
    elif N1 == 2:
        C = "З"
    if N2 == 1:
        C = "С"
    elif N2 == -1:
        C = "Ю"
    elif N2 == 2:
        C = "З"
print("Новая ориентация локатора:", C)

#5.14--------------------------------------------------------------------------------------------
print("5.14")
print('''Дано целое число N и набор из N вещественных чисел. Вывести в
том же порядке округленные значения всех чисел из данного набора
(как целые числа), а также сумму всех округленных значений.
''')

n = int(input("Введите N: "))

i = 1
sumNumbers = 0
roundNumbers = ""

while i <= n:
    num = float(input(f"Введите {i} число: "))
    num = round(num)
    sumNumbers += num
    roundNumbers += str(num) + " "
    i += 1


print("Ответ: ")
print(f"Округленные числа: {roundNumbers}")
print(f"Сумма округленных числел: {sumNumbers}")

#5.15--------------------------------------------------------------------------------------------
print("#5.15")
print('''Дано целое число N и набор из N целых чисел. Вывести в том же
порядке номера всех нечетных чисел из данного набора и
количество K таких чисел.
''')

n = int(input("Введите N: "))
i = 1

oddsInd = ""
quantity = 0

while i <= n:
    num = int(input(f"Введите {i} число: "))

    if num % 2 != 0:
        oddsInd += str(i) + " "
        quantity += 1
    i += 1

print("Ответ:")
print(f"Номера нечетных чисел: {oddsInd}")
print(f"Количество нечетных чисел: {quantity}")

#5.17--------------------------------------------------------------------------------------------
print("#5.17")
print('''Дано целое число N и набор из N целых чисел, упорядоченный по
возрастанию. Данный набор может содержать одинаковые
элементы. Вывести в том же порядке все различные элементы
данного набора
''')

n = int(input("Введите N: "))
i = 1

elements = ""
prev = -1

while i <= n:

    current = int(input(f"Введите {i} число: "))
    
    if elements == "":
        elements += str(current) + " "
        prev = current
    else:
        if prev != current:
            elements += str(current) + " "
            prev = current
    i += 1

print(f"Различные элементы: {elements}")

#5.18--------------------------------------------------------------------------------------------
print("#5.18")
print('''Дано целое число N и набор из N целых чисел, содержащий по
крайней мере два нуля. Вывести сумму чисел из данного набора,
расположенных между последними двумя нулями (если последние
нули идут подряд, то вывести 0).
''')

n = int(input("Введите число N: "))
i = 1
sumBetweenZeroes = 0
sumCurrent = 0

while i <= n:
    num = int(input(f"Введите {i} число: "))

    sumCurrent += num

    if (num == 0):
        sumBetweenZeroes = sumCurrent
        sumCurrent = 0
    
    i += 1

print(f"Ответ: Сумма между последними двумя нулями: {sumBetweenZeroes}")   