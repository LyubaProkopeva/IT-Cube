# Задание №12
numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)