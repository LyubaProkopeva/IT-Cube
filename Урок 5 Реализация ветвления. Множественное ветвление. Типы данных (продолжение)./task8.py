# Задание №8
s = input()
ind = s.find('@')
print('Нет' if ind == -1 or s[ind+1:].find('.') == -1 else 'Ок')