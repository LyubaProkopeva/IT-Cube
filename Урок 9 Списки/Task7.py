# Задание №7
num_strings = int(input())
strings = []
for _ in range(num_strings):
    string = input()
    strings.append(string)
word = input()
for i in strings:
    if word in i:
        print(i)