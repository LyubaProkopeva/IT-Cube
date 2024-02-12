# Задание №3
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (b1 == a2):
    print(b1)
elif (b2 == a1):
    print(b2)
elif (b1 < a2 or b2 < a1):
    print('Пустое множество')
else:
    print(max(a1, a2), min(b1, b2))