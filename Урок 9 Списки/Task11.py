# Задание №11
words = input().split()
if len(words) < 2:
    print()
else:
    min_word, max_word = min(words, key=len), max(words, key=len)
    min_index, max_index = words.index(min_word), words.index(max_word)
    words[min_index], words[max_index] = max_word, min_word
    print(*words)