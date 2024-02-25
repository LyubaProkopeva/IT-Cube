# Задание №6
x = int(input())
a = x // 100
b = x % 10
c = (x // 10)% 10
z = (a + b + c) - min(a, b, c) - max(a, b, c)
if (max(a, b, c) - min(a, b, c)) == z:
    print('Прикольное')
else:
    print('Не прикольное')