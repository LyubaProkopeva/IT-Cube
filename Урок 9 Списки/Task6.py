# Задание №6
num_strings = int(input())
strings = []
for _ in range(num_strings):
    string = input()
    strings.append(string)

from collections import Counter
counter = Counter(strings)
print(*counter)