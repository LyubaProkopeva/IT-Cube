# Задание №4
n = int(input("Введите количество карточек: "))
sum_of_cards = sum(map(int, input("Введите номера оставшихся карточек через пробел: ").split()))
missing_card = n*(n+1)//2 - sum_of_cards
print("Потерянная карточка имеет номер", missing_card)