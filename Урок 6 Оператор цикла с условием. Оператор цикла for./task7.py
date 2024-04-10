#Задание №7 Я немного добавила к условиям вдруг окажется так, что нет цифр кратных двум.
n = int(input())
a = n % 2
while n > 0:
    digit = n % 2
    if digit % 2 == 0:
        if digit > a:
            a = digit
    n = n // 2
if a == 0:
    print("Нет")
else:
    print(a)