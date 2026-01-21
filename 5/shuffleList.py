import random

cards = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

shuffled = random.shuffle(cards)

for card in cards:
    print(card, end=" ")