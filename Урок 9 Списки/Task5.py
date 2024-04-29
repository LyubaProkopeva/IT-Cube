# Задание №5
num_strings = int(input())
strings = []
for _ in range(num_strings):
    string = input()
    strings.extend(string)
print(strings)