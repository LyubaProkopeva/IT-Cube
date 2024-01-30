# Задание №4
name = int(input()) 
a = name // 100 
b = name % 100 // 10
c = name % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='') 
print(c, a, b, sep='')
print(c, b, a, sep='')