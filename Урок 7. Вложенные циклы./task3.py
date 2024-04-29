# Задание №3
x = int(input())
y = int(input())
a = 0
for i in range(x, y + 1):
    i1 = True
    for j in range(2, i):
        if i % j == 0:
            i1 = False
            break
    if i1:
        a += 1
print("Найдено простых чисел: ", a)    