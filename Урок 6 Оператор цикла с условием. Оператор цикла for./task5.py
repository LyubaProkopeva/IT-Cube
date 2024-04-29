# Задание №5
list=[]
l2 = 0
max1 = 0
max2 = 0
max3 = 0
while True:
    l=input()
    if l == 'СТОП': 
        break
    l1 = int(l)
    if l1>max1:
        max3=max2
        max2=max1
        max1 = l1
    if l1<max1 and l1>max2:
        max3=max2
        max2=l1
    if l1<max1 and l1<max2 and l1>max3:
        max3=l1        
print(max1,max2,max3)