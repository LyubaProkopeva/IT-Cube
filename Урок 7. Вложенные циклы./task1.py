# Задание №1
n = int(input())
if n > 0:
    for i in range(1, n+1): 
        k = 1            
        for j in range(1, int(i / 2) + 1):
            if i % j == 0:
                k += 1
        print(i, '-', k)