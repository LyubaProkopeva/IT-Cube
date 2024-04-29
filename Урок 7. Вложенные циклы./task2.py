# Задание №2
n = int(input())
m = 0
for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
        f = f * j
        print('i = ', i, ' j = ', j,' f = ', f, 'm = ', m )
    m = m + f
print(m)    