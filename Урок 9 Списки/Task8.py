# Задание №8
user_input = input()
def numbers_above_50(input_string):
    numbers = input_string.split()
    count = 0 
    for number in numbers:
            if int(number) > 50:
                count += 1
    return count
result = numbers_above_50(user_input)
print(result)