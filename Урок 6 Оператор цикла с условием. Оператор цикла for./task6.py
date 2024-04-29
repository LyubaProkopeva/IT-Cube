# Задание №6
n=int(input()) 
f1=1
f2=1
i=0
print(f1, end = ' ')
while i<n-1:
    print(f2, end = ' ')
    f3=f2+f1
    f1=f2
    f2=f3
    i+=1