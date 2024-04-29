# Задание №10
numbers = list(map(int, input().split()))
if len(numbers) < 2:
    print()
else:
    mini, maxi = min(numbers), max(numbers)
    min_index, max_index = numbers.index(mini), numbers.index(maxi)
    numbers[min_index], numbers[max_index] = maxi, mini
    print(numbers)