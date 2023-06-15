print("Задача 4.3.")

dist = 100
distInDay = 10
sumDist = 0
count = 0

while sumDist <= dist:
    sumDist += distInDay
    distInDay = distInDay + distInDay / 10
    count += 1

print(f"Суммарный пробег превысит 100 км на {count} день")