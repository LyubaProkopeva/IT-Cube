# Задание №2
a = int(input())
b = int(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '**':
    print(a ** b)
elif c == '/':
    if b == 0:
        print('Делить на 0 нельзя')
    else:
        print(a / b)
elif c == '//':
    if b == 0:
        print('Делить на 0 нельзя')
    else:
        print(a // b)
elif c == '%':
    if b == 0:
        print('Делить на 0 нельзя')
    else:
        print(a % b)