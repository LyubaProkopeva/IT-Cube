# Задание №1
num = int(input())
list = []
if num>0: 
    for i in range(1, num+1):
        list.append(i)
    print(list)
else:
    print('Ошибка!')