import math

print("Задача 2.9.")

R = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))

ring = math.pi * R * R
rectangle = a * a

if ring > rectangle:
    print("Площадь круга больше площади квадрата")
elif ring < rectangle:
    print("Площадь квадрата больше площади круга")
else:
    print("Площади круга и квадрата равны")