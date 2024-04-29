# Задание №3
t = list("abcdefghijklmnopqrstuvwxyz")
x = [letter * (index + 1) for index, letter in enumerate(t)]
print(x)