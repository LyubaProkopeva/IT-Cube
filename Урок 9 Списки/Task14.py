# Творческое задание №1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [29, 35, 25, 11, 22, 41, 100]
bubble_sort(arr)
print( arr)