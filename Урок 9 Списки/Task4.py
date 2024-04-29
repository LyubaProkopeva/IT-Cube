# Задание №4
num = int(input())
a = []
for _ in range(num):
    s = input()
    a.append(s)
num_find = int(input())
for s in a:
    if num_find <= len(s) and num_find > 0:
        print(s[num_find - 1], end='')
    else:
        print(f"В слове '{s}' меньше {num_find} букв")